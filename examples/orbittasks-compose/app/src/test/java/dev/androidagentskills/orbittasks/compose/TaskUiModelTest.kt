package dev.androidagentskills.orbittasks.compose

import org.junit.Assert.assertEquals
import org.junit.Test

class TaskUiModelTest {
    @Test
    fun status_is_preserved() {
        val task = TaskUiModel(title = "Ship adapters", status = "Done")
        assertEquals("Done", task.status)
    }
}
