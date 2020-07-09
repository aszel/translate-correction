# Translation files correction tool

## Description

The tool creates a file for each language which holds all duplicate values
with an array of the referring keys.

Example
```json
"Prozess": ["global.process", "timetrack.process", "production-plan.process", "queue-administration.process", "cdc.queue-properties.processName"],
```

The term "Prozess" is being used several times for the German language.
We end up with a file for each language named "duplicates.LANGUAGE.json".

These files get read. Since German holds the most duplicates we loop over
all duplicate entries and grab the first referring key for each duplicate
value.

For each value we try to find a match in the other language duplicate files and
create a dictionary for each first key. This provides a nice overview of the current
status.

Example
```json
"global.process": {
  "de": ["global.process", "timetrack.process", "production-plan.process", "queue-administration.process", "cdc.queue-properties.processName"],
  "en": ["global.process", "timetrack.process", "production-plan.process", "queue-administration.process"],
  "pl": ["global.process", "queue-administration.process"]
},
```

See "inter-language-duplicates.json" for details.

## Usage

Run duplicate-finder.py for each language (I am too lazy to polish this ATM)
```
python duplicate-finder.py
```
After this is done run the inter language program
```
python inter-language-duplicate-finder.py
```
