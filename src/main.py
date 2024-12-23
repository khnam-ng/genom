import numpy as np
from downloader import download_genome

#@title ARRAY: ORGANISMS_NAME_LIST
organisms = [
    "Aeropyrum pernix K1",
    "Archaeoglobus fulgidus DSM 4304",
    "Archaeoglobus profundus DSM 5631",
    "Caldivirga maquilingensis IC-167",
    "Candidatus Korarchaeum cryptofilum OPF8",
    "Candidatus Methanoregula boonei 6A8",
    "Candidatus Methanosphaerula palustris E1-9c",
    "Cenarchaeum symbiosum A",
    "Desulfurococcus kamchatkensis 1221n",
    "Haloarcula marismortui ATCC 43049",
    "Haloarcula marismortui ATCC 43049",
    "Halobacterium sp. NRC-1",
    "Halomicrobium mukohataei DSM 12286",
    "Haloquadratum walsbyi DSM 16790",
    "Halorhabdus utahensis DSM 12940",
    "Halorubrum lacusprofundi ATCC 49239",
    "Halorubrum lacusprofundi ATCC 49239",
    "Haloterrigena turkmenica DSM 5511",
    "Hyperthermus butylicus DSM 5456",
    "Ignicoccus hospitalis KIN4/I",
    "Metallosphaera sedula DSM 5348",
    "Methanobrevibacter ruminantium M1",
    "Methanocaldococcus fervens AG86",
    "Methanocella paludicola SANAE",
    "Methanococcoides burtonii DSM 6242",
    "Methanococcus aeolicus Nankai-3",
    "Methanococcus maripaludis C6",
    "Methanococcus vannielii SB",
    "Methanocorpusculum labreanum Z",
    "Methanoculleus marisnigri JR1",
    "Methanopyrus kandleri AV19",
    "Methanosaeta thermophila PT",
    "Methanosarcina acetivorans C2A",
    "Methanosarcina barkeri str. Fusaro",
    "Methanosarcina mazei Go1",
    "Methanosphaera stadtmanae DSM 3091",
    "Methanospirillum hungatei JF-1",
    "Nanoarchaeum equitans Kin4-M",
    "Natronomonas pharaonis DSM 2160",
    "Nitrosopumilus maritimus SCM1",
    "Picrophilus torridus DSM 9790",
    "Pyrobaculum aerophilum str. IM2",
    "Pyrobaculum arsenaticum DSM 13514",
    "Pyrococcus abyssi GE5",
    "Pyrococcus furiosus DSM 3638",
    "Pyrococcus horikoshii OT3",
    "Staphylothermus marinus F1",
    "Sulfolobus acidocaldarius DSM 639",
    "Sulfolobus solfataricus P2",
    "Thermococcus gammatolerans EJ3",
    "Thermofilum pendens Hrk 5",
    "Thermoplasma acidophilum DSM 1728",
    "Thermoplasma volcanium GSS1",
    "Thermoproteus neutrophilus V24Sta",
    "Acholeplasma laidlawii PG-8A",
    "Acidobacterium capsulatum ATCC 51196",
    "Akkermansia muciniphila ATCC BAA-835",
    "Alicyclobacillus acidocaldarius subsp. acidocaldarius DSM 446",
    "Aquifex aeolicus VF5",
    "Bacillus cereus Q1",
    "Bacillus pseudofirmus OF4",
    "Bacteroides fragilis YCH46",
    "Bdellovibrio bacteriovorus HD100",
    "Bordetella pertussis Tohama I",
    "Borrelia burgdorferi B31",
    "Campylobacter jejuni subsp. jejuni 81-176",
    "Candidatus Amoebophilus asiaticus 5a2",
    "Candidatus Cloacamonas acidaminovorans",
    "Candidatus Endomicrobium sp. Rs-D17",
    "Carboxydothermus hydrogenoformans Z-2901",
    "Chlamydia trachomatis 434/Bu",
    "Chlorobium chlorochromatii CaD3",
    "Chloroflexus aurantiacus J-10-fl",
    "Clostridium acetobutylicum ATCC 824",
    "Corynebacterium glutamicum ATCC 13032",
    "Coxiella burnetii RSA 493",
    "Cupriavidus taiwanensis",
    "Cupriavidus taiwanensis",
    "Cyanothece sp. ATCC 51142",
    "Cyanothece sp. ATCC 51142",
    "Dehalococcoides ethenogenes 195",
    "Deinococcus radiodurans R1",
    "Deinococcus radiodurans R1",
    "Dictyoglomus thermophilum H-6-12",
    "Elusimicrobium minutum Pei191",
    "Fibrobacter succinogenes subsp. succinogenes S85",
    "Flavobacterium psychrophilum JIP02/86",
    "Fusobacterium nucleatum subsp. nucleatum ATCC 25586",
    "Gemmata obscuriglobus UQM 2246",
    "Gemmatimonas aurantiaca T-27",
    "Gloeobacter violaceus PCC 7421",
    "Leptospira interrogans serovar Lai str. 56601",
    "Leptospira interrogans serovar Lai str. 56601",
    "Magnetococcus sp. MC-1",
    "Methylacidiphilum infernorum V4",
    "Mycoplasma genitalium G37",
    "Nostoc punctiforme PCC 73102",
    "Opitutus terrae PB90-1",
    "Pedobacter heparinus DSM 2366",
    "Pirellula staleyi DSM 6068",
    "Prochlorococcus marinus str. AS9601",
    "Psychrobacter arcticus 273-4",
    "Rhizobium leguminosarum bv. trifolii WSM1325",
    "Rhodopirellula baltica SH 1",
    "Rhodospirillum rubrum ATCC 11170",
    "Rickettsia rickettsii str. Iowa",
    "Shewanella putrefaciens CN-32",
    "Solibacter usitatus Ellin6076",
    "Synechococcus elongatus PCC 6301",
    "Thermanaerovibrio acidaminovorans DSM 6589",
    "Thermoanaerobacter tengcongensis MB4",
    "Thermobaculum terrenum ATCC BAA-798",
    "Thermobaculum terrenum ATCC BAA-798",
    "Thermodesulfovibrio yellowstonii DSM 11347",
    "Thermomicrobium roseum DSM 5159",
    "Thermotoga maritima MSB8"
]

if __name__ == "__main__":
    #@title Download 10 genomes and save them into array before making its k-mers signatures.
    genomes_size = 10
    seqs_dict = {}
    indexes = np.random.randint(len(organisms), size=genomes_size)
    for index in indexes:
        seqs_dict[index] = organisms[index]

    print('indexes:', indexes)
    print('len(seqs_dict):', len(seqs_dict))