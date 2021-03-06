# Ingest HCA to ENA

Converts HCA pre-ingest JSON to ENA XML and packages it as a zip.

## Test
Tests take an example output, generates ENA XML files and validates each against ENA schemas. The XML files are then packaged into a zip file.

## Run at the command line
```
handler.py ./examples/metadata_spleen_v5_20180313_userFriendlyHeaders.json
```

Will create a directory in `/tmp` containing the XML and a corresponding ZIP of the directory.

## Run Lambda Locally
```
serverless invoke local --function convert --path ./examples/metadata_spleen_v5_20180313_userFriendlyHeaders.json
```

## Deployment
The code is also deployed as a AWS Lambda with a HTTP endpoint. 

## Example cURL
```
curl -X POST \
  https://n8b51jauvh.execute-api.us-east-1.amazonaws.com/dev/convert \
  -H 'Accept: application/zip' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '[ {
  "schema_type" : "project",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/project/5.0.1/project",
    "schema_version" : "5.0.1",
    "schema_type" : "project",
    "project_core" : {
      "project_shortname" : "Tissue_stability",
      "project_title" : "Testing ischaemic sensitivity of human tissue using single cell RNA seq",
      "project_description" : "Assessment of ischaemic sensitivity of three human tissues using 10x 3'\'' single cell RNA sequencing - this submission is ONLY for the first spleen sample; further samples to be collected.  Ultimately we aim to collect data from three tissues expected to have different sensitivity to ischaemia: spleen (expected least sensitive), oesophagus (in the middle) and liver (expected most sensitive).  Samples will be collected '\''fresh'\'' (ie as soon as possible) and at 12h, 24h and 72h post onset of ischaemia in the donor.  Single cell RNA sequencing data will be generated at each time point using the 10x genomics single cell 3'\'' method.",
      "describedBy" : "https://schema.humancellatlas.org/core/project/5.0.0/project_core",
      "schema_version" : "5.0.0"
    },
    "supplementary_files" : [ "Experimental_report.docx", "Human_spleen_dissociation_protocol.pdf", "Clinical_metadata.xlsx", "284C_IMAGE_spleen_annotated.jpeg", "10x_protocol.pdf" ]
  } ]
}, {
  "schema_type" : "biomaterial",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/donor_organism",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "284C-A1",
      "biomaterial_name" : "284C-spleen",
      "biomaterial_description" : "Spleen",
      "ncbi_taxon_id" : [ 9606 ],
      "supplementary_files" : [ "Clinical_metadata.xlsx" ],
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "death" : {
      "cause_of_death" : "Hypoxic brain damage",
      "describedBy" : "https://schema.humancellatlas.org/module/biomaterial/5.0.0/death"
    },
    "medical_history" : {
      "alcohol_history" : "3-6 units/day",
      "smoking_history" : "Smoker, 20/day for 25 years, stopped 2000",
      "describedBy" : "https://schema.humancellatlas.org/module/biomaterial/5.0.0/medical_history"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "organism_age" : "55-60",
    "organism_age_unit" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/time_unit_ontology",
      "text" : "year"
    },
    "development_stage" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/development_stage_ontology",
      "text" : "adult"
    },
    "disease" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/disease_ontology",
      "text" : "normal"
    } ],
    "height" : "1.75-1.8",
    "height_unit" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/length_unit_ontology",
      "text" : "meter"
    },
    "is_living" : false,
    "biological_sex" : "male",
    "weight" : "80-85",
    "weight_unit" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/mass_unit_ontology",
      "text" : "kg"
    }
  } ],
  "links" : [ {
    "source_type" : "biomaterial",
    "source_id" : "284C-A1",
    "destination_type" : "process",
    "destination_ids" : [ "" ]
  } ]
}, {
  "schema_type" : "biomaterial",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/specimen_from_organism",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL5",
      "biomaterial_name" : "284C_spleen_fresh",
      "biomaterial_description" : "fresh spleen",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "284C-A1",
      "supplementary_files" : [ "284C_IMAGE_spleen_annotated.jpeg" ],
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "organ" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_ontology",
      "text" : "spleen"
    },
    "organ_part" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_part_ontology",
      "text" : "spleen"
    },
    "state_of_specimen" : {
      "gross_image" : [ "284C_IMAGE_spleen_annotated.jpg" ],
      "ischemic_time" : 7200,
      "postmortem_interval" : 19800,
      "describedBy" : "https://schema.humancellatlas.org/module/biomaterial/5.0.0/state_of_specimen"
    }
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/specimen_from_organism",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL6",
      "biomaterial_name" : "284C_spleen_12h",
      "biomaterial_description" : "spleen at 12h ischaemic time",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "284C-A1",
      "supplementary_files" : [ "284C_IMAGE_spleen_annotated.jpeg" ],
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "organ" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_ontology",
      "text" : "spleen"
    },
    "organ_part" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_part_ontology",
      "text" : "spleen"
    },
    "state_of_specimen" : {
      "gross_image" : [ "284C_IMAGE_spleen_annotated.jpg" ],
      "ischemic_time" : 43200,
      "postmortem_interval" : 54300,
      "describedBy" : "https://schema.humancellatlas.org/module/biomaterial/5.0.0/state_of_specimen"
    }
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/specimen_from_organism",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL7",
      "biomaterial_name" : "284C_spleen_24h",
      "biomaterial_description" : "spleen at 24h ischaemic time",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "284C-A1",
      "supplementary_files" : [ "284C_IMAGE_spleen_annotated.jpeg" ],
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "organ" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_ontology",
      "text" : "spleen"
    },
    "organ_part" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_part_ontology",
      "text" : "spleen"
    },
    "state_of_specimen" : {
      "gross_image" : [ "284C_IMAGE_spleen_annotated.jpg" ],
      "ischemic_time" : 86400,
      "postmortem_interval" : 97200,
      "describedBy" : "https://schema.humancellatlas.org/module/biomaterial/5.0.0/state_of_specimen"
    }
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/specimen_from_organism",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL8",
      "biomaterial_name" : "284C_spleen_72h",
      "biomaterial_description" : "spleen at 72h ischaemic time",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "284C-A1",
      "supplementary_files" : [ "284C_IMAGE_spleen_annotated.jpeg" ],
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "organ" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_ontology",
      "text" : "spleen"
    },
    "organ_part" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/organ_part_ontology",
      "text" : "spleen"
    },
    "state_of_specimen" : {
      "gross_image" : [ "284C_IMAGE_spleen_annotated.jpg" ],
      "ischemic_time" : 259200,
      "postmortem_interval" : 269100,
      "describedBy" : "https://schema.humancellatlas.org/module/biomaterial/5.0.0/state_of_specimen"
    }
  } ],
  "links" : [ {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL5",
    "destination_type" : "organ",
    "destination_ids" : [ "UBERON:0002106" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL5",
    "destination_type" : "process",
    "destination_ids" : [ "enrichment_process_1" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL6",
    "destination_type" : "organ",
    "destination_ids" : [ "UBERON:0002106" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL6",
    "destination_type" : "process",
    "destination_ids" : [ "enrichment_process_1" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL7",
    "destination_type" : "organ",
    "destination_ids" : [ "UBERON:0002106" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL7",
    "destination_type" : "process",
    "destination_ids" : [ "enrichment_process_1" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL8",
    "destination_type" : "organ",
    "destination_ids" : [ "UBERON:0002106" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL8",
    "destination_type" : "process",
    "destination_ids" : [ "enrichment_process_1" ]
  } ]
}, {
  "schema_type" : "biomaterial",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/cell_suspension",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL5_cells",
      "biomaterial_name" : "cells from fresh spleen",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "A1-Spl-0-TL5",
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "total_estimated_cells" : 39300000
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/cell_suspension",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL6_cells",
      "biomaterial_name" : "cells from spleen at 12h ischaemic time",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "A1-Spl-0-TL6",
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "total_estimated_cells" : 25200000
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/cell_suspension",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL7_cells",
      "biomaterial_name" : "cells from spleen at 24h ischaemic time",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "A1-Spl-0-TL7",
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "total_estimated_cells" : 65240000
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/biomaterial/5.0.0/cell_suspension",
    "schema_version" : "5.0.0",
    "schema_type" : "biomaterial",
    "biomaterial_core" : {
      "biomaterial_id" : "A1-Spl-0-TL8_cells",
      "biomaterial_name" : "cells from spleen at 72h ischaemic time",
      "ncbi_taxon_id" : [ 9606 ],
      "has_input_biomaterial" : "A1-Spl-0-TL8",
      "describedBy" : "https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core",
      "schema_version" : "5.0.0"
    },
    "genus_species" : [ {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/species_ontology",
      "text" : "Homo sapiens"
    } ],
    "total_estimated_cells" : 39250000
  } ],
  "links" : [ {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL5_cells",
    "destination_type" : "process",
    "destination_ids" : [ "" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL6_cells",
    "destination_type" : "process",
    "destination_ids" : [ "" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL7_cells",
    "destination_type" : "process",
    "destination_ids" : [ "" ]
  }, {
    "source_type" : "biomaterial",
    "source_id" : "A1-Spl-0-TL8_cells",
    "destination_type" : "process",
    "destination_ids" : [ "" ]
  } ]
}, {
  "schema_type" : "process",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/process/biomaterial_collection/5.0.0/dissociation_process",
    "schema_version" : "5.0.0",
    "schema_type" : "process",
    "process_core" : {
      "process_id" : "dissociation_process_1",
      "process_name" : "Dissociation of spleen tissue sample into cell suspension",
      "describedBy" : "https://schema.humancellatlas.org/core/process/5.0.0/process_core",
      "schema_version" : "5.0.0"
    },
    "dissociation_method" : "mechanical",
    "nucleic_acid_source" : "single cell"
  } ],
  "links" : [ {
    "source_type" : "process",
    "source_id" : "dissociation_process_1",
    "destination_type" : "protocol",
    "destination_ids" : [ "Human_spleen_dissociation_protocol" ]
  } ]
}, {
  "schema_type" : "process",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/process/biomaterial_collection/5.0.0/enrichment_process",
    "schema_version" : "5.0.0",
    "schema_type" : "process",
    "process_core" : {
      "process_id" : "enrichment_process_1",
      "process_name" : "Enrichment for live cells",
      "describedBy" : "https://schema.humancellatlas.org/core/process/5.0.0/process_core",
      "schema_version" : "5.0.0"
    },
    "enrichment_method" : "MACS",
    "markers" : "LiveCells"
  } ],
  "links" : [ {
    "source_type" : "process",
    "source_id" : "enrichment_process_1",
    "destination_type" : "protocol",
    "destination_ids" : [ "Human_spleen_dissociation_protocol" ]
  } ]
}, {
  "schema_type" : "process",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/process/sequencing/5.0.0/library_preparation_process",
    "schema_version" : "5.0.0",
    "schema_type" : "process",
    "process_core" : {
      "process_id" : "library_preparation_process_1",
      "describedBy" : "https://schema.humancellatlas.org/core/process/5.0.0/process_core",
      "schema_version" : "5.0.0"
    },
    "input_nucleic_acid_molecule" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/biological_macromolecule_ontology",
      "text" : "polyA RNA"
    },
    "library_construction_approach" : "10x_v2",
    "end_bias" : "3 prime tag",
    "strand" : "second"
  } ],
  "links" : [ {
    "source_type" : "process",
    "source_id" : "library_preparation_process_1",
    "destination_type" : "cell",
    "destination_ids" : [ "Read 1" ]
  }, {
    "source_type" : "process",
    "source_id" : "library_preparation_process_1",
    "destination_type" : "cell",
    "destination_ids" : [ "0" ]
  }, {
    "source_type" : "process",
    "source_id" : "library_preparation_process_1",
    "destination_type" : "cell",
    "destination_ids" : [ "16" ]
  }, {
    "source_type" : "process",
    "source_id" : "library_preparation_process_1",
    "destination_type" : "umi",
    "destination_ids" : [ "Read 1" ]
  }, {
    "source_type" : "process",
    "source_id" : "library_preparation_process_1",
    "destination_type" : "umi",
    "destination_ids" : [ "16" ]
  }, {
    "source_type" : "process",
    "source_id" : "library_preparation_process_1",
    "destination_type" : "umi",
    "destination_ids" : [ "10" ]
  }, {
    "source_type" : "process",
    "source_id" : "library_preparation_process_1",
    "destination_type" : "protocol",
    "destination_ids" : [ "10x_sequencing_protocol" ]
  } ]
}, {
  "schema_type" : "process",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/process/sequencing/5.0.0/sequencing_process",
    "schema_version" : "5.0.0",
    "schema_type" : "process",
    "process_core" : {
      "process_id" : "sequencing_process_1",
      "process_name" : "10x_v2 sequencing",
      "describedBy" : "https://schema.humancellatlas.org/core/process/5.0.0/process_core",
      "schema_version" : "5.0.0"
    },
    "instrument_manufacturer_model" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/instrument_ontology",
      "text" : "Illumina HiSeq 4000"
    },
    "paired_ends" : true
  } ],
  "links" : [ {
    "source_type" : "process",
    "source_id" : "sequencing_process_1",
    "destination_type" : "protocol",
    "destination_ids" : [ "10x_sequencing_protocol" ]
  } ]
}, {
  "schema_type" : "protocol",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/protocol/5.0.0/protocol",
    "schema_version" : "5.0.0",
    "schema_type" : "protocol",
    "protocol_core" : {
      "protocol_id" : "Human_spleen_dissociation_protocol",
      "protocol_name" : "Spleen dissociation protocol",
      "document" : "Human_spleen_dissociation_protocol.pdf",
      "describedBy" : "https://schema.humancellatlas.org/core/protocol/5.0.0/protocol_core",
      "schema_version" : "5.0.0"
    },
    "protocol_type" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/protocol_type_ontology",
      "text" : "EFO:0003809"
    }
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/protocol/5.0.0/protocol",
    "schema_version" : "5.0.0",
    "schema_type" : "protocol",
    "protocol_core" : {
      "protocol_id" : "10x_sequencing_protocol",
      "protocol_name" : "10X Genomics protocol - including loading single cells and library prep",
      "protocol_description" : "ChromiumTM Single Cell 3'\'' Library & Gel Bead Kit v2",
      "document" : "10x_protocol.pdf",
      "describedBy" : "https://schema.humancellatlas.org/core/protocol/5.0.0/protocol_core",
      "schema_version" : "5.0.0"
    },
    "protocol_type" : {
      "describedBy" : "https://schema.humancellatlas.org/module/ontology/5.0.0/protocol_type_ontology",
      "text" : "EFO:0007832"
    }
  } ]
}, {
  "schema_type" : "file",
  "content" : [ {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S1_L001_I1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "index1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S1_L001_R1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S1_L001_R2_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read2",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S2_L001_I1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "index1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S2_L001_R1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S2_L001_R2_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read2",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S3_L001_I1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "index1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S3_L001_R1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S3_L001_R2_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read2",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S4_L001_I1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "index1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S4_L001_R1_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read1",
    "lane_index" : 1
  }, {
    "describedBy" : "https://schema.humancellatlas.org/type/file/5.0.0/sequence_file",
    "schema_version" : "5.0.0",
    "schema_type" : "file",
    "file_core" : {
      "file_name" : "HCATisStabAug177078016_S4_L001_R2_001.fastq.gz",
      "file_format" : "fastq.gz",
      "describedBy" : "https://schema.humancellatlas.org/core/file/5.0.0/file_core",
      "schema_version" : "5.0.0"
    },
    "read_index" : "read2",
    "lane_index" : 1
  } ],
  "links" : [ {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S1_L001_I1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S1_L001_I1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S1_L001_R1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S1_L001_R1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S1_L001_R2_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S1_L001_R2_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S2_L001_I1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S2_L001_I1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S2_L001_R1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S2_L001_R1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S2_L001_R2_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S2_L001_R2_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S3_L001_I1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S3_L001_I1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S3_L001_R1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S3_L001_R1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S3_L001_R2_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S3_L001_R2_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S4_L001_I1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S4_L001_I1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S4_L001_R1_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S4_L001_R1_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S4_L001_R2_001.fastq.gz",
    "destination_type" : "biomaterial",
    "destination_ids" : [ "A1-Spl-0-TL5_cells" ]
  }, {
    "source_type" : "file",
    "source_id" : "HCATisStabAug177078016_S4_L001_R2_001.fastq.gz",
    "destination_type" : "sequencing",
    "destination_ids" : [ "sequencing_process_1" ]
  } ]
} ]'
```
