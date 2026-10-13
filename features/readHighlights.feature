Feature: Read Highlights
	Tests related to Read Highlights

	Scenario: I want to read about a highlight.
		Given this is the first time I am using the website
    When Click the navigate button
    And Click the <highlight_name> button
    Then An image is present
    And Text is show including <key_sentence>
		Examples:
			| highlight_name | key_sentence |
			| i2 Group | The application was able to chart up to 500,000 nodes and edges. |
