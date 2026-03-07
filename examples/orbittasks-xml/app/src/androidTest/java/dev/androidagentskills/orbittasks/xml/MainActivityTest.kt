package dev.androidagentskills.orbittasks.xml

import android.widget.TextView
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Assert.assertEquals
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class MainActivityTest {
    @get:Rule
    val rule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun shows_header() {
        rule.scenario.onActivity { activity ->
            val header = activity.findViewById<TextView>(R.id.header)
            assertEquals("OrbitTasks XML", header.text.toString())
        }
    }
}
