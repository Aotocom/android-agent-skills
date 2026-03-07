package dev.androidagentskills.orbittasks.compose

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.FilterChip
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SnackbarHost
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp

data class TaskUiModel(val title: String, val status: String)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { OrbitTasksApp() }
    }
}

@Composable
private fun OrbitTasksApp() {
    val tasks = listOf(
        TaskUiModel("Prepare beta release notes", "Today"),
        TaskUiModel("Sync offline edits", "Waiting"),
        TaskUiModel("Check notification permission", "Blocked"),
    )
    val selectedFilter = remember { mutableStateOf("All") }
    val snackbarHostState = remember { SnackbarHostState() }

    MaterialTheme {
        Scaffold(snackbarHost = { SnackbarHost(snackbarHostState) }) { innerPadding ->
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding)
                    .padding(20.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp),
            ) {
                Text("OrbitTasks", style = MaterialTheme.typography.headlineMedium)
                Text("Compose showcase fixture for skills and CI.")
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    listOf("All", "Due", "Blocked").forEach { label ->
                        FilterChip(
                            selected = selectedFilter.value == label,
                            onClick = { selectedFilter.value = label },
                            label = { Text(label) },
                        )
                    }
                }
                Card(modifier = Modifier.fillMaxWidth()) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text("Reminder readiness", style = MaterialTheme.typography.titleMedium)
                        Text("Notification permission is not granted. Use the permissions skill before scheduling background reminders.")
                        Button(onClick = {}, modifier = Modifier.padding(top = 12.dp)) {
                            Text("Review blocked state")
                        }
                    }
                }
                LazyColumn(verticalArrangement = Arrangement.spacedBy(12.dp)) {
                    items(tasks) { task ->
                        Card(
                            modifier = Modifier
                                .fillMaxWidth()
                                .semantics { contentDescription = "Task card ${task.title}" },
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text(task.title, style = MaterialTheme.typography.titleMedium)
                                Text(task.status, style = MaterialTheme.typography.bodyMedium)
                            }
                        }
                    }
                }
            }
        }
    }
}
