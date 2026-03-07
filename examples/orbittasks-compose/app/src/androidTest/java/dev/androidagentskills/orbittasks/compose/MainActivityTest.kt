package dev.androidagentskills.orbittasks.compose

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithText
import org.junit.Rule
import org.junit.Test

class MainActivityTest {
    @get:Rule
    val rule = createAndroidComposeRule<MainActivity>()

    @Test
    fun shows_key_copy() {
        rule.onNodeWithText("OrbitTasks").assertIsDisplayed()
        rule.onNodeWithText("Reminder readiness").assertIsDisplayed()
    }
}
