"""
argparse template.
Not meant to be imported.
Just copy, paste, and reuse.

Author: Bradley T. Martin
"""
def get_args():
	"""
	Parse command-line arguments. Imported with argparse.
	Returns: object of command-line arguments.
	"""
	parser = argparse.ArgumentParser(description="Convert VCF file to BGC format (with genotype uncertainties). Currently only handles three populations maximum (P1, P2, and Admixed).", add_help=False)

	required_args = parser.add_argument_group("Required Arguments")
	optional_args = parser.add_argument_group("Optional Arguments")

	## Required Arguments
	required_args.add_argument("-v", "--vcf",
								type=str,
								required=True,
								help="Input VCF file")
	required_args.add_argument("-m", "--popmap",
								type=str,
								required=True,
								help="Two-column tab-separated population map file: inds\tpops. No header line.")
	required_args.add_argument("--p1",
								type=str,
								required=True,
								help="Parental population 1")
	required_args.add_argument("--p2",
								type=str,
								required=True,
								help="Parental population 2")
	required_args.add_argument("--admixed",
								type=str,
								required=True,
								help="Admixed population (limit=1 population)")
	optional_args.add_argument("-o", "--outprefix",
								type=str,
								required=False,
								default="bgc",
								help="Specify output prefix for BGC files.")
	optional_args.add_argument("-l", "--linkage",
								default = True, action="store_false")
	optional_args.add_argument("-h", "--help",
								action="help",
								help="Displays this help menu")

	if len(sys.argv)==1:
		print("\nExiting because no command-line options were called.\n")
		parser.print_help(sys.stderr)
		sys.exit(1)

	args = parser.parse_args()
	return args