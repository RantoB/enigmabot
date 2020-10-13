## introduction
* greet
  - utter_greet
> check_if_question_or_riddle

## introduction and bot propose riddle
* greet
  - utter_greet_and_propose_riddle
> check_answer_about_riddle

## deny riddle proposition and suggest question on ENIGMA Stras
> check_answer_about_riddle
* deny
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras_after_riddle

## deny question on ENIGMA Stras and propose riddle
> check_answer_about_ENIGMA_Stras
* deny
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## deny question on ENIGMA Stras and bye
> check_answer_about_ENIGMA_Stras_after_riddle
* deny
  - utter_thanks
  - utter_goodbye
* goodbye
  - utter_goodbye

## deny riddle proposition and bye
> check_answer_about_riddle_after_question_ENIGMA_Stras
* deny
  - utter_thanks
  - utter_goodbye
* goodbye
  - utter_goodbye

## WTF 
* WTF
  - action_default_fallback

## goodbye
* goodbye
  - utter_thanks
  - utter_goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
