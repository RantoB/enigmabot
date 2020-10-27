## introduction
* ENIGMA_bot_presentation
- utter_presentation

## Greetings
* greet
  - utter_greet

## deny riddle proposition and suggest FAQ
> check_answer_about_riddle
* deny
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras_after_riddle

## deny FAQ and propose riddle
> check_answer_about_ENIGMA_Stras
* deny
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## deny FAQ after riddle, suggest subscribe
> check_answer_about_ENIGMA_Stras_after_riddle
* deny
  - utter_subscribe
> check_answer_about_subscribe

## deny riddle proposition after FAQ, suggest subscribe
> check_answer_about_riddle_after_question_ENIGMA_Stras
* deny
  - utter_subscribe
> check_answer_about_subscribe

## End
> check_answer_about_subscribe
* deny
  - utter_thanks
  - utter_goodbye
* goodbye
  - utter_goodbye

## No question
* no_question
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## WTF
* WTF
  - action_default_fallback

## goodbye
* goodbye
  - utter_thanks
  - utter_goodbye
* goodbye
  - utter_goodbye

## kiss and goodbye
* kiss
  - utter_thanks
  - utter_goodbye
* goodbye
  - utter_goodbye

## insults
* insults
  - utter_keep_calm
* insults
  - utter_keep_calm
* insults
  - utter_goodbye
