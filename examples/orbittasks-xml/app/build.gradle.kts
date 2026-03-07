plugins {
  id("com.android.application")
}

android {
  namespace = "dev.androidagentskills.orbittasks.xml"
  compileSdk = 36

  defaultConfig {
    applicationId = "dev.androidagentskills.orbittasks.xml"
    minSdk = 26
    targetSdk = 36
    versionCode = 1
    versionName = "0.1.0"
    testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
  }

  buildFeatures {
    viewBinding = true
  }

  compileOptions {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
  }

  testOptions {
    unitTests.isIncludeAndroidResources = true
  }
}

dependencies {
  implementation("androidx.activity:activity-ktx:1.12.4")
  implementation("androidx.appcompat:appcompat:1.7.1")
  implementation("androidx.core:core-ktx:1.15.0")
  implementation("androidx.constraintlayout:constraintlayout:2.2.1")
  implementation("org.jetbrains.kotlin:kotlin-stdlib:2.2.10")

  testImplementation("junit:junit:4.13.2")
  androidTestImplementation("androidx.test.ext:junit:1.2.1")
  androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
}
