import json
import os
from datetime import datetime


class SectionOne:
    def __init__(self, input_file: str):
        if os.path.isfile(input_file):
            with open(input_file, 'r') as f:
                self.all_candidates = json.load(f)
        else:
            raise FileNotFoundError

    def present(self) -> None:
        for candidate in self.all_candidates:
            if candidate['experience']:
                full_output = f'Hello {candidate["contact_info"]["name"]["formatted_name"]}\n\n'
                sorted_experience = sorted(candidate['experience'],
                                           key=lambda cand: datetime.strptime(cand['start_date'], '%b/%d/%Y'))
                last_exp = None
                for experience in sorted_experience:
                    if last_exp:
                        last_end_date = datetime.strptime(last_exp['end_date'], '%b/%d/%Y')
                        curr_start_date = datetime.strptime(experience['start_date'], '%b/%d/%Y')
                        full_output += f'Gap in CV for {(curr_start_date - last_end_date).days} Days\n'
                    else:
                        last_exp = experience
                    full_output += f'Worked as: {experience["title"]}, '
                    if experience['current_job']:
                        full_output += f'Since {experience["start_date"]}'
                    else:
                        full_output += f'From {experience["start_date"]} To {experience["end_date"]} '

                    full_output += f'in {experience["location"]["short_display_address"]}\n'
            else:
                full_output = f'Hello {candidate["contact_info"]["name"]["formatted_name"]}\n\nNo work experience found'
            print(full_output)


file_path = 'input.json'
section_obj = SectionOne(file_path)

section_obj.present()
