# import argparse
import Bio

#@title FUNCTION: DOWNLOAD_GENOME(organism)
def download_genome(organism_name):
  try:
    # Step 1: Search for the organism's genome in the NCBI nucleotide database
    print(f"Searching for complete genome of {organism_name}...")
    search_handle = Bio.Entrez.esearch(
        db="nucleotide",  # Search the nucleotide database
        term=f"{organism_name}[Organism] AND complete genome[Title]",
        retmax=1  # Retrieve only the top result
    )
    search_results = Bio.Entrez.read(search_handle)
    search_handle.close()

    # Get the first GenBank ID (if found)
    if not search_results["IdList"]:
        print(f"No complete genome found for {organism_name}.")
        return

    genome_id = search_results["IdList"][0]
    print(f"Found genome with GenBank ID: {genome_id}")

    # Step 2: Fetch the genome data in FASTA format
    print("Downloading genome in FASTA format...")
    fetch_handle = Bio.Entrez.efetch(
        db="nucleotide",
        id=genome_id,
        rettype="fasta",
        retmode="text"
    )
    genome_seq = fetch_handle.read()
    fetch_handle.close()
    print(f"Genome is successfully downloaded.")

    return organism_name, genome_seq

  except Exception as e:
    print(f"An error occurred: {e}")


