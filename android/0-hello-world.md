# Hello World Codelab

[Codelab](https://developer.android.com/codelabs/basic-android-kotlin-compose-first-app)

## Topics

- How to create an Android App with Android Studio
- How to run apps with the Preview tool in Android Studio
- How to update text with Kotlin
- How to update a User Interface (UI) with Jetpack Compose
- How to see a preview of your app with Preview in Jetpack Compose

## Notes

`onCreate()` calls other functions to build the user interface, and is the starting point of execution in Android
- `setContent()` within `onCreate()` defines the layout through composable functions
- `@Composable` functions generate UI, and can be called from `setContent()` or other composable functions
- `@Preview` renders your composable in the `Design` tab in Android Studio without having to build the entire app

To surround the `Text` in the codelab with a `Surface`, we pressed `Alt Enter` and selected `Surround with widget -> Surround wih Container`

A `Modifier` is used to decorate a composable.
- Every composable's first optional parameter should be a `Modifier`

## Summary

- To create a new project:
    - open Android Studio,
    - click `New Project > Empty Activity > Next`,
    - enter a name for your project and then
    - configure its settings.
- To see how your app looks, use the Preview pane.
- Composable functions are like regular functions with a few differences: functions names are capitalized, you add the `@Composable` annotation before the function, `@Composable` functions can't return anything.
- A `Modifier` is used to augment or decorate your composable.
