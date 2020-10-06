## introduction
* greet
  - utter_greet
  <!-- - utter_greet_and_name
* inform_name{"person":"Bertrand"} OR inform_name
  - action_introduction
* deny OR affirm
  - action_introduction_input_to_confirm
* inform_name{"person":"Bertrand"} OR inform_name
  - action_force_introduction -->

## general deny
* deny
  - utter_sth_else
* deny
  - utter_before_end
  - utter_goodbye

## general affirm
* affirm
  - utter_question

## goodbye
* goodbye
  - utter_before_end
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
