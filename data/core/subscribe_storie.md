## subscribe request from user
* how_to_subscribe
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information

## Normal subscribe
> check_answer_about_subscribe
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information

## subscribe & Fallback action & continue form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - action_default_fallback
* inform_name OR inform_email
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information

## subscribe & stop & continue form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* stop OR deny
  - utter_ask_leave_subscribe_form
* deny
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information

## subscribe & stop & leave form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* stop OR deny
  - utter_ask_leave_subscribe_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras_after_subscribe

## subscribe & FAQ & continue form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* faq
  - respond_faq
  - utter_ask_leave_subscribe_form
* deny
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information

## subscribe & FAQ & leave form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* faq
  - respond_faq
  - utter_ask_leave_subscribe_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras_after_subscribe

## subscribe & OOS & continue form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_subscribe_form
* deny
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information

## subscribe & OOS & leave form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_subscribe_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras_after_subscribe

## subscribe & game presentation & continue form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* question_pitch
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game
  - utter_ask_leave_subscribe_form
* deny
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information

## subscribe & game presentation & leave form
* affirm
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* question_pitch
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game
  - utter_ask_leave_subscribe_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras_after_subscribe

## information confirmed
> user_check_information
* affirm
  - action_save_information
  - utter_question_on_ENIGMA_Stras
> check_answer_about_ENIGMA_Stras_after_subscribe

## information not confirmed
> user_check_information
* deny
  - action_reset_subscribe_slots
  - utter_correct_info
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
  - action_ask_user_to_check_infomration
> user_check_information
