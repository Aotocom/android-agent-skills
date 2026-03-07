package dev.androidagentskills.orbittasks.xml

import android.os.Bundle
import androidx.activity.ComponentActivity
import dev.androidagentskills.orbittasks.xml.databinding.ActivityMainBinding

class MainActivity : ComponentActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.header.text = "OrbitTasks XML"
        binding.summary.text = "View-system fixture for legacy rescue, permissions, and migration skills."
        binding.status.text = "Notification permission pending"
    }
}
