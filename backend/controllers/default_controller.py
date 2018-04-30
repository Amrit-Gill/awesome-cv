import connexion
import six

from models.cv import CV  # noqa: E501
import util

from generator.generate_tex_source import GenerateTexSource

def generate_cv(body):  # noqa: E501
    """Generate CV

     # noqa: E501

    :param body: Json schema of CV
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        cv_body = CV.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            return GenerateTexSource().generate(cv_body)
        except Exception as e:
            return "An InternalServerErrorException occurred: {}".format(e), 500
    else:
        return "Request is not json", 400
