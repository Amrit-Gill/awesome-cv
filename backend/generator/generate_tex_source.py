import logging
import os
import base64
from pdf2image import convert_from_path

from generator import tex_templates
from generator.compile_and_build_pdf import CompileAndBuildPdf

SCRIPT_DIR = os.path.dirname(__file__)
MAIN_TEMPLATE = "resume_workspace\main_template.tex"
EDUCATION = "resume_workspace\cv-sections\education.tex"
EXPERIENCE = "resume_workspace\cv-sections\experience.tex"
SKILLS = "resume_workspace\cv-sections\skills.tex"
PDF_FILENAME = "resume_workspace\main_template.pdf"
OUTPUT_IMAGE = "resume_workspace\page"

class GenerateTexSource:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate(self, cv_body):
        main_template = self.build_main_template(cv_body)
        education_template = self.build_education_template(cv_body)
        experience_template = self.build_experience_template(cv_body)
        skills_template = self.build_skills_template(cv_body)
        tex_main_file = open(os.path.join(SCRIPT_DIR, os.pardir, MAIN_TEMPLATE), 'w')
        tex_education = open(os.path.join(SCRIPT_DIR, os.pardir, EDUCATION), 'w')
        tex_experience = open(os.path.join(SCRIPT_DIR, os.pardir, EXPERIENCE), 'w')
        tex_skills = open(os.path.join(SCRIPT_DIR, os.pardir, SKILLS), 'w')
        tex_main_file.write(main_template)
        tex_education.write(education_template)
        tex_experience.write(experience_template)
        tex_skills.write(skills_template)

        tex_main_file.close()
        tex_education.close()
        tex_experience.close()
        tex_skills.close()

        # CompileAndBuildPdf().compile(os.path.join(SCRIPT_DIR, os.pardir, MAIN_TEMPLATE))

        pages = convert_from_path(os.path.join(SCRIPT_DIR, os.pardir, PDF_FILENAME), 100)
        count = 0
        for page in pages:
            count = count + 1
            name = "".join([os.path.join(SCRIPT_DIR, os.pardir, OUTPUT_IMAGE), str(count)])
            page.save("".join([name, '.jpg']), 'JPEG')

        with open("".join([os.path.join(SCRIPT_DIR, os.pardir, OUTPUT_IMAGE), "1", ".jpg"]), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string

    def build_main_template(self, cv_body):
        template = tex_templates.main_template % {"name": cv_body.name, "address": cv_body.address,
                                                  "phone_number": cv_body.mobile, "email": cv_body.email,
                                                  "github": cv_body.github, "linkedin": cv_body.linkedin,
                                                  "skype": cv_body.skype, "position": cv_body.position}
        print(template)
        return template

    def build_education_template(self, cv_body):
        cv_entries = ""
        for education_entries in cv_body.education:
            cv_entry = tex_templates.education_cv_entries % {"title": education_entries.title, "school": education_entries.school,
                                                               "address": education_entries.address, "start_date": education_entries.start_date,
                                                               "end_date": education_entries.end_date}
            cv_entries = '\n'.join([cv_entries, cv_entry])
        education = tex_templates.education % {"cv_entries": cv_entries}
        print(education)
        return education

    def build_experience_template(self, cv_body):
        experience_cv_entries = ""
        for experience in cv_body.experience:
            items = ""
            for detail in experience.details:
                item = tex_templates.experience_items % {"item": detail.value}
                items = "\n".join([items, item])
            experience_cv_entry = tex_templates.experience_cv_entries %{"title": experience.title, "company": experience.company,
                                                               "address": experience.address, "start_date": experience.start_date,
                                                               "end_date": experience.end_date, "items": items}
            experience_cv_entries = "\n".join([experience_cv_entries, experience_cv_entry])
        experience = tex_templates.experience % {"cv_entries": experience_cv_entries}
        print(experience)
        return experience

    def build_skills_template(self, cv_body):
        items = ""
        for skill in cv_body.skills:
            item = tex_templates.skill_items %{"title": skill.title, "value": skill.values}
            items = "\n".join([items, item])
        skills = tex_templates.skills %{"skill_items": items}
        print(skills)
        return skills
