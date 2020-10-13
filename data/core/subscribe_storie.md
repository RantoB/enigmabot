## subscribe
* how_to_subscribe
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
> user_check_information

## subscribe with information confirmed
> user_check_information
* affirm
  - action_save_information
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras

## subscribe with information confirmed
> user_check_information
* deny
  - action_reset_subscribe_slots
  - utter_correct_info
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
> user_check_information
