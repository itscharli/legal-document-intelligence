# Document taxonomy — draft v0.1

Status: initial design, not validated against a corpus. Updated October 19, 2026.

## Scope and structure

Initial focus: California state-court employment litigation and related administrative and pre-litigation material. Federal litigation, arbitration, class/representative actions, and appeals are extension areas requiring further source review. This is a classification design, not a statement of filing requirements or an exhaustive legal checklist.

Assign one primary family and one subtype per document component. Store litigation stage, subject matter, and filing status separately. A declaration supporting a motion remains a declaration; a payroll record attached as an exhibit remains a payroll record.

| Family ID | Family | Initial subtypes |
| --- | --- | --- |
| PRE | Pre-litigation | demand_letter; preservation_notice; settlement_offer; agency_intake; agency_complaint; agency_response; right_to_sue_notice; agency_determination |
| PLD | Pleadings | complaint; amended_complaint; answer; amended_answer; cross_complaint; answer_to_cross_complaint |
| SVC | Service and notice | summons; proof_of_service; notice_of_acknowledgment_of_receipt; notice_of_entry; hearing_notice; deposition_notice; other_notice |
| ADM | Case administration | civil_case_cover_sheet; case_management_statement; scheduling_document; notice_of_related_case; substitution_of_attorney; dismissal_request; docket_entry |
| DSC | Written discovery | form_interrogatories; special_interrogatories; requests_for_production; requests_for_admission; interrogatory_responses; production_responses; admission_responses; supplemental_responses; discovery_objections; privilege_log; meet_and_confer |
| DEP | Testimony and subpoenas | deposition_transcript; deposition_errata; subpoena; subpoena_objection; deposition_exhibit_index |
| EVD | Underlying evidence | employment_agreement; arbitration_agreement; personnel_record; policy_or_handbook; payroll_record; time_record; benefits_record; performance_record; disciplinary_record; termination_record; accommodation_record; leave_record; workplace_complaint; investigation_record; email; message; medical_record; photograph; audio; video; other_business_record |
| MOT | Requests for court relief | motion; application; ex_parte_application; opposition; reply; memorandum_of_points_and_authorities; separate_statement; evidentiary_objections; request_for_judicial_notice; proposed_order |
| SUP | Supporting and procedural papers | declaration; affidavit; exhibit_cover; exhibit_index; stipulation; proposed_stipulation; certificate; other_supporting_paper |
| CRT | Court-issued documents | order; minute_order; tentative_ruling; judgment; court_notice; hearing_transcript |
| ADR | Settlement and alternative dispute resolution | mediation_brief; settlement_agreement; release; settlement_conference_statement; arbitration_demand; arbitration_response; arbitration_award |
| TRL | Trial | trial_brief; motion_in_limine; witness_list; exhibit_list; proposed_jury_instructions; verdict_form; special_verdict; trial_transcript; statement_of_decision |
| PST | Post-judgment and appellate | memorandum_of_costs; writ_of_execution; notice_of_appeal; appellate_brief; appellate_record; appellate_opinion; remittitur |
| UNK | Unresolved | unknown; other; mixed_unsegmented |

These are candidate labels. A listed type may have no suitable public example. Sensitive evidence categories describe potential coverage, not permission to collect or publish records.

## Separate attributes

- Stage: pre_litigation, administrative, pleadings, discovery, dispositive_motion, pretrial, trial, post_judgment, appeal, mixed, unknown.
- Subject tags (multi-value): discrimination, harassment, retaliation, wage_hour, wrongful_termination, accommodation, leave, contract, arbitration, class_action, representative_action, other, unknown.
- Motion topic (when applicable): demurrer, strike, compel_discovery, protective_order, summary_judgment, summary_adjudication, compel_arbitration, class_certification, settlement_approval, attorney_fees, new_trial, other, unknown.
- Document status: blank_template, draft, proposed, filed, issued, executed, unknown.
- Container role: standalone, lead_document, attachment, embedded_component.
- Forum: california_state_court, california_agency, federal_court, federal_agency, arbitration, other, unknown.

## Boundary rules

1. Distinguish a civil complaint from an agency complaint by recipient and document function.
2. Classify a demurrer under MOT.motion with motion_topic=demurrer; preserve the original title.
3. Distinguish a proposed order from an issued order using visible status evidence. Do not assume a signature means the court issued it.
4. A notice of motion and its memorandum may require separate components. If reliable page boundaries cannot be identified, use UNK.mixed_unsegmented and request review.
5. Evidence produced in discovery retains its underlying type; record discovery as the stage or context.
6. Use other for an understood type missing from the vocabulary; use unknown when the type cannot be determined.
7. Store form number separately from document type. Blank official forms are templates, not completed case documents.
8. Never infer legal merit, timeliness, privilege, or truth from a classification label.

## Source anchors and coverage gaps

Reviewed October 19, 2026. These sources anchor selected categories; they do not validate every candidate label above.

- [California Courts forms directory](https://selfhelp.courts.ca.gov/find-forms/all-by-category): form-based categories, including case management.
- [California Courts discovery forms](https://selfhelp.courts.ca.gov/find-forms?query=discovery+and+subpoenas): employment form interrogatories (DISC-002) and discovery/subpoena materials.
- [California Courts discovery overview](https://selfhelp.courts.ca.gov/discovery-civil/request): discovery document families.
- [California Civil Rights Department right-to-sue materials](https://calcivilrights.ca.gov/obtainrighttosue/): agency complaints and right-to-sue notices.

Next review: verify remaining categories against official forms and rules; review wage/representative-action, arbitration, federal, and appellate coverage; test confusing label pairs on public examples. Do not describe this draft as covering every litigation document type.
