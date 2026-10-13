Feature: Copy Key Information
	Tests related to Copy Key Information

	Scenario: I want to copy key information
		Given this is the first time I am using the website
		When I click the copy button next to <key_information>
    Then The copy button next to <key_information> turns <confirm_color>
		And <key_information> is added to clipboard
		Examples:
			| key_information | confirm_color |
			| +44 7354430588 | fill-lime-500 |
      | steven_herlihy@yahoo.com | fill-lime-500 |
