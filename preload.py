def preload(parser):
	parser.add_argument(
		"--distributed-remotes",
		nargs="+",
		help="Enter n pairs of sockets",
		type=lambda t: t.split(":")
	)

	parser.add_argument(
		"--distributed-skip-verify-remotes",
		help="Disable verification of remote worker TLS certificates",
		action="store_true"
	)

	parser.add_argument(
		"--distributed-remotes-autosave",
		help="Enable auto-saving of remote worker generations",
		action="store_true"
	)

	parser.add_argument(
		"--distributed-debug",
		help="Enable debug information",
		action="store_true"
	)
