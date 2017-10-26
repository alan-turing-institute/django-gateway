from jobs.models import Script, Input, Parameter, Family, Job


def get_attribute_list(model):
    attribute_list = \
        [a for a in vars(model) if not a.startswith('_')]
    return attribute_list


def parameter_template_to_parameter(parameter_template):
    parameter = Parameter()
    attribute_list = get_attribute_list(parameter_template)
    for attribute in attribute_list:
        source = getattr(parameter_template, attribute)
        setattr(parameter, attribute, source)
    return parameter


def family_template_to_family(family_template):
    family = Family()
    family.save()

    family.label = family_template.label
    family.name = family_template.name
    # family.collapse = family_template.collapse

    for parameter_template in family_template.parameters.all():
        family.parameters.add(
            parameter_template_to_parameter(parameter_template), bulk=False
        )

    return family


def script_template_to_script(script_template):
    script = Script()
    attribute_list = get_attribute_list(script_template)
    for attribute in attribute_list:
        source = getattr(script_template, attribute)
        setattr(script, attribute, source)
    return script


def input_template_to_input(input_template):
    input_ = Input()
    attribute_list = get_attribute_list(input_template)
    for attribute in attribute_list:
        source = getattr(input_template, attribute)
        setattr(input_, attribute, source)
    return input_


def case_to_job(case, job_id=None):

    # TODO assigning a primary key at instantiation requires
    # calls to Job.save() in order to build up object

    # job = Job(pk=job_id)
    job = Job()
    job.save()

    job.description = case.job.description
    job.name = case.job.name

    for family_template in case.job.families.all():
        job.families.add(family_template_to_family(family_template), bulk=False)

    for script_template in case.job.scripts.all():
        job.scripts.add(script_template_to_script(script_template), bulk=False)

    for input_template in case.job.inputs.all():
        job.inputs.add(input_template_to_input(input_template), bulk=False)

    return job
