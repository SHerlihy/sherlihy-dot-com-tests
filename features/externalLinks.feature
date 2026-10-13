Feature: External Links
	Tests related to External Links

	Scenario: I want to visit linked websites
		Given this is the first time I am using the website
		When I click the <link_name> link
		Then <link_address> is visited
		Examples:
			| link_name | link_address |
			| LLM Learning | https://d2gru0zoilocfa.cloudfront.net/ |
