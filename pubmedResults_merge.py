import json

filenames = ['COI_range10k.json',
             'COI_range20k.json',
             'COI_range30k.json',
             'COI_range40k.json',
             'COI_range50k.json',
             'COI_range60k.json',
             'COI_range70k.json',
             'COI_range80k.json',
             'COI_range90k.json',
             'COI_range100k.json',
             'COI_range110k.json',
             'COI_range120k.json',
             'COI_range130k.json',
             'COI_range140k.json',
             'COI_range150k.json',
             'COI_range160k.json',
             'COI_range170k.json',
             'COI_range180k.json',
             'COI_range190k.json',
             'COI_range200k.json',
             'COI_range210k.json',
             'COI_range220k.json',
             'COI_range230k.json',
             'COI_range240k.json',
             'COI_range250k.json',
             'COI_range260k.json',
             'COI_range270k.json',
             'COI_range280k.json',
             'COI_range290k.json',
             'COI_range300k.json',
             'COI_range310k.json',
             'COI_range320k.json',
             'COI_range330k.json',
             'COI_range340k.json',
             'COI_range350k.json',
             'COI_range360k.json',
             'COI_range370k.json',
             'COI_range380k.json',
             'COI_range390k.json',
             'COI_range400k.json',
             'COI_range410k.json',
             'COI_range420k.json',
             'COI_range428593k.json'
             ]



with open ('mergedCOIS_121719.json', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

            
