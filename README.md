# Ingest HCA to ENA

Converts HCA pre-ingest JSON to ENA XML

## Test
Tests take an example output, generate XML files and validate them against ENA schemas.

## Run Locally

```
serverless invoke local --function convert --path ./examples/metadata_spleen_v5_20180313_userFriendlyHeaders.json
```
