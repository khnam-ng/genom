import argparse
from Bio import Entrez
from Bio import SeqIO

# Set your email address for Entrez (required by NCBI policies)
Entrez.email = "your_email@example.com"

# Function to search and download genome sequences
def download_genome(organism_name, output_file):
    try:
        # Step 1: Search for the organism's genome in the NCBI nucleotide database
        print(f"Searching for complete genome of {organism_name}...")
        search_handle = Entrez.esearch(
            db="nucleotide",  # Search the nucleotide database
            term=f"{organism_name}[Organism] AND complete genome[Title]",
            retmax=1  # Retrieve only the top result
        )
        search_results = Entrez.read(search_handle)
        search_handle.close()

        # Get the first GenBank ID (if found)
        if not search_results["IdList"]:
            print(f"No complete genome found for {organism_name}.")
            return

        genome_id = search_results["IdList"][0]
        print(f"Found genome with GenBank ID: {genome_id}")

        # Step 2: Fetch the genome data in FASTA format
        print("Downloading genome in FASTA format...")
        fetch_handle = Entrez.efetch(
            db="nucleotide",
            id=genome_id,
            rettype="fasta",
            retmode="text"
        )

        # Write the FASTA file to the output
        with open(output_file, "w") as output:
            output.write(fetch_handle.read())

        fetch_handle.close()
        print(f"Genome successfully downloaded and saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Command-line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a complete genome in FASTA format from NCBI.")
    parser.add_argument("organism", type=str, help="Name of the organism (e.g., 'Escherichia coli').")
    parser.add_argument("output_file", type=str, help="Output file name for the genome (e.g., 'genome.fasta').")

    args = parser.parse_args()

    download_genome(args.organism, args.output_file)

