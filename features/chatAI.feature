Feature: Chat AI
	Tests related to Chat AI

	Scenario: I want to query the AI
		Given this is the first time I am using the website
		When I input my <query> into the input box
		And I click the submit button
		Then My <query> is shown in the chat section
		And The answer is shown below my query
		Examples:
			| query |
			| what languages does he have experience in? |
