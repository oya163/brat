'''
Annotation specification file, used to determine possible choices and for
verifying the correctness by the verifier.

Author:     Sampo Pyysalo
Version:    2011-01-20
'''

#TODO: These are really constants, upper-case the names, remember to make
# the other files that import them conform too.
#TODO: Silly, but : placement isn't really standard.

## Configuration for annotation types and semantics

# Types of textbounds representing physical entities.
physical_entity_types = [
    'Protein',
    'Entity',
    'Organism',
    'Chemical',
    'Two-component-system',
    'Regulon-operon',
    ]

# Allowed nestings for physical entities.
allowed_entity_nestings = {
    'default'              : [],
    'Two-component-system' : ['Protein'],
    'Organism'             : ['Protein', 'Chemical', 'Two-component-system'],
    'Regulon-operon'       : ['Protein'],
    }

# Arguments allowed for events, by type. Derived from the tables on
# the per-task pages under http://sites.google.com/site/bionlpst/ .

# abbrevs
theme_only_argument = {
        'Theme' : ['Protein'],
        }

theme_and_site_arguments = {
        'Theme' : ['Protein'],
        'Site'  : ['Entity'],
        }

regulation_arguments = {
        'Theme' : ['Protein', 'event'],
        'Cause' : ['Protein', 'event'],
        'Site'  : ['Entity'],
        'CSite' : ['Entity'],
        }

localization_arguments = {
        'Theme' : ['Protein'],
        'AtLoc' : ['Entity'],
        'ToLoc' : ['Entity'],
        }

sidechain_modification_arguments = {
        'Theme'     : ['Protein'],
        'Site'      : ['Entity'],
        'Sidechain' : ['Entity'],
        }

contextgene_modification_arguments = {
    'Theme'       : ['Protein'],
    'Site'        : ['Entity'],
    'Contextgene' : ['Protein'],
    }

event_argument_types = {
    # GENIA
    'default'             : theme_only_argument,
    'Phosphorylation'     : theme_and_site_arguments,
    'Localization'        : localization_arguments,
    'Binding'             : theme_and_site_arguments,
    'Regulation'          : regulation_arguments,
    'Positive_regulation' : regulation_arguments,
    'Negative_regulation' : regulation_arguments,

    # EPI
    'Dephosphorylation'   : theme_and_site_arguments,
    'Hydroxylation'       : theme_and_site_arguments,
    'Dehydroxylation'     : theme_and_site_arguments,
    'Ubiquitination'      : theme_and_site_arguments,
    'Deubiquitination'    : theme_and_site_arguments,
    'DNA_methylation'     : theme_and_site_arguments,
    'DNA_demethylation'   : theme_and_site_arguments,
    'Glycosylation'       : sidechain_modification_arguments,
    'Deglycosylation'     : sidechain_modification_arguments,
    'Acetylation'         : contextgene_modification_arguments,
    'Deacetylation'       : contextgene_modification_arguments,
    'Methylation'         : contextgene_modification_arguments,
    'Demethylation'       : contextgene_modification_arguments,
    'Catalysis'           : regulation_arguments,

    # More PTM
    'Palmitoylation'      : theme_and_site_arguments,

    # TODO: this is a temporary workaround extension for PIR annotation
    # revision. Implement a proper solution.
    'PTM'                 : theme_and_site_arguments,

    # TODO: ID
    }

# Types of textbounds that should not overlap with others of their
# type.
no_sametype_overlap_textbound_types = physical_entity_types[:]
