param(
  [string]$agent = "codex",
  [string]$scope = "user",
  [string]$skill = "all"
)

$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$python = Get-Command python3 -ErrorAction SilentlyContinue
if (-not $python) {
  $python = Get-Command python -ErrorAction SilentlyContinue
}
if (-not $python) {
  throw "Python is required to build adapters before install."
}
& $python.Source (Join-Path $root "scripts/build_adapters.py") --agent all | Out-Null

switch ($agent) {
  "codex" {
    $target = if ($scope -eq "project") { Join-Path (Get-Location) "skills" } else { Join-Path $HOME ".codex/skills" }
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    if ($skill -eq "all") {
      Copy-Item -Recurse -Force (Join-Path $root "skills\*") $target
    } else {
      Copy-Item -Recurse -Force (Join-Path $root "skills\$skill") $target
    }
  }
  "claude" {
    $target = if ($scope -eq "project") { Join-Path (Get-Location) ".claude/agents" } else { Join-Path $HOME ".claude/agents" }
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    if ($skill -eq "all") {
      Copy-Item -Recurse -Force (Join-Path $root ".claude/agents\*") $target
    } else {
      Copy-Item -Force (Join-Path $root ".claude/agents\$skill.md") $target
    }
  }
  "cursor" {
    $target = if ($scope -eq "project") { Join-Path (Get-Location) ".cursor/rules" } else { Join-Path $HOME ".cursor/rules" }
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    if ($skill -eq "all") {
      Copy-Item -Recurse -Force (Join-Path $root ".cursor/rules\*") $target
    } else {
      Copy-Item -Force (Join-Path $root ".cursor/rules\$skill.mdc") $target
    }
  }
  default {
    throw "Unsupported agent: $agent"
  }
}

Write-Output "Installed $skill for $agent ($scope)"
