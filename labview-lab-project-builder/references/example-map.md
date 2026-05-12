# LabVIEW Example Map

Use this map to choose real `.vi` files from an installed LabVIEW distribution before creating a coursework package.

## Signal Generation, Filtering, FFT

Search:

```powershell
rg --files "<LabVIEW>\examples\Signal Processing" | rg -i "waveform|filter|spectrum|FFT|DSA|noise"
```

Useful examples:

- `Signal Processing\Waveform Measurements\Dynamic Signal Analyzer (sim).vi`
- `Signal Processing\Waveform Measurements\Amplitude Spectrum (sim).vi`
- `Signal Processing\Waveform Measurements\Noise Waveforms and PS Density.vi`
- `Signal Processing\Waveform Conditioning\IIR Filtering and Response.vi`
- `Signal Processing\Waveform Conditioning\FIR Filtering and Response.vi`
- `Signal Processing\Filters\IIR Filter Design.vi`
- `Signal Processing\Filters\FIR Windowed Filter Design.vi`

## Arrays and Strings

Search:

```powershell
rg --files "<LabVIEW>\examples" | rg -i "array|string|search|sort|byte|character"
```

Useful examples:

- `Arrays\Build Array.vi`
- `Arrays\Replace Array Elements.vi`
- `Arrays\Separate Array Values.vi`
- `Strings\Concatenate Strings.vi`
- `Strings\String Length.vi`
- `Strings\Extract Numbers with Match Pattern.vi`
- `Waveform\Waveform - Search.vi`

## Real-Time Monitoring and Control

Use the complete example tree:

```text
Industry Applications\Temperature Monitoring
```

Important files:

- `Temperature Monitoring.vi`
- `Temperature Monitoring.lvproj`
- `support\Simulate Temperature Acquisition.vi`
- `support\Set Alarm Colors and Get Alarm Text.vi`
- `support\Message Queue\Temp Monitor Message Queue.lvlib`
- `support\User Event - Stop\Temp Monitor User Event - Stop.lvlib`
- `controls\Temp Monitor UI Data.ctl`
- `controls\Simulated Data.ctl`

## UI, Audio, Python, Gesture, Picture

Useful examples:

- `Structures\Event Structure\Handling Common User Interface Events.vi`
- `Structures\Event Structure\Handling Mouse Events.vi`
- `Graphics and Sound\Sound\Continuous Sound Input.vi`
- `Graphics and Sound\Sound\Sound Input to File.vi`
- `Connectivity\Python\PythonNode_ConcatenateTwoStrings.vi`
- `Connectivity\Python\PythonNode_AddTwoIntegers.vi`
- `Channels\Messenger\Mouse Gesture Handler with Messenger Channel.vi`
- `Channels\Messenger\Gesture\Recognize Gesture.vi`
- `Graphics and Sound\2D Picture Control\Annotating a Picture.vi`

## Web Searches

Use web search only when installed examples are insufficient or a current connector/tool is needed. Prefer official NI documentation and examples. Do not rely on random `.vi` binaries from untrusted sites.
