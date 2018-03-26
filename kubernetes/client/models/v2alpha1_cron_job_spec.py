# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V2alpha1CronJobSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'concurrency_policy': 'str',
        'failed_jobs_history_limit': 'int',
        'job_template': 'V2alpha1JobTemplateSpec',
        'schedule': 'str',
        'starting_deadline_seconds': 'int',
        'successful_jobs_history_limit': 'int',
        'suspend': 'bool'
    }

    attribute_map = {
        'concurrency_policy': 'concurrencyPolicy',
        'failed_jobs_history_limit': 'failedJobsHistoryLimit',
        'job_template': 'jobTemplate',
        'schedule': 'schedule',
        'starting_deadline_seconds': 'startingDeadlineSeconds',
        'successful_jobs_history_limit': 'successfulJobsHistoryLimit',
        'suspend': 'suspend'
    }

    def __init__(self, concurrency_policy=None, failed_jobs_history_limit=None, job_template=None, schedule=None, starting_deadline_seconds=None, successful_jobs_history_limit=None, suspend=None):
        """
        V2alpha1CronJobSpec - a model defined in Swagger
        """

        self._concurrency_policy = None
        self._failed_jobs_history_limit = None
        self._job_template = None
        self._schedule = None
        self._starting_deadline_seconds = None
        self._successful_jobs_history_limit = None
        self._suspend = None
        self.discriminator = None

        if concurrency_policy is not None:
          self.concurrency_policy = concurrency_policy
        if failed_jobs_history_limit is not None:
          self.failed_jobs_history_limit = failed_jobs_history_limit
        self.job_template = job_template
        self.schedule = schedule
        if starting_deadline_seconds is not None:
          self.starting_deadline_seconds = starting_deadline_seconds
        if successful_jobs_history_limit is not None:
          self.successful_jobs_history_limit = successful_jobs_history_limit
        if suspend is not None:
          self.suspend = suspend

    @property
    def concurrency_policy(self):
        """
        Gets the concurrency_policy of this V2alpha1CronJobSpec.
        Specifies how to treat concurrent executions of a Job. Valid values are: - \"Allow\" (default): allows CronJobs to run concurrently; - \"Forbid\": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - \"Replace\": cancels currently running job and replaces it with a new one

        :return: The concurrency_policy of this V2alpha1CronJobSpec.
        :rtype: str
        """
        return self._concurrency_policy

    @concurrency_policy.setter
    def concurrency_policy(self, concurrency_policy):
        """
        Sets the concurrency_policy of this V2alpha1CronJobSpec.
        Specifies how to treat concurrent executions of a Job. Valid values are: - \"Allow\" (default): allows CronJobs to run concurrently; - \"Forbid\": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - \"Replace\": cancels currently running job and replaces it with a new one

        :param concurrency_policy: The concurrency_policy of this V2alpha1CronJobSpec.
        :type: str
        """

        self._concurrency_policy = concurrency_policy

    @property
    def failed_jobs_history_limit(self):
        """
        Gets the failed_jobs_history_limit of this V2alpha1CronJobSpec.
        The number of failed finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified.

        :return: The failed_jobs_history_limit of this V2alpha1CronJobSpec.
        :rtype: int
        """
        return self._failed_jobs_history_limit

    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, failed_jobs_history_limit):
        """
        Sets the failed_jobs_history_limit of this V2alpha1CronJobSpec.
        The number of failed finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified.

        :param failed_jobs_history_limit: The failed_jobs_history_limit of this V2alpha1CronJobSpec.
        :type: int
        """

        self._failed_jobs_history_limit = failed_jobs_history_limit

    @property
    def job_template(self):
        """
        Gets the job_template of this V2alpha1CronJobSpec.
        Specifies the job that will be created when executing a CronJob.

        :return: The job_template of this V2alpha1CronJobSpec.
        :rtype: V2alpha1JobTemplateSpec
        """
        return self._job_template

    @job_template.setter
    def job_template(self, job_template):
        """
        Sets the job_template of this V2alpha1CronJobSpec.
        Specifies the job that will be created when executing a CronJob.

        :param job_template: The job_template of this V2alpha1CronJobSpec.
        :type: V2alpha1JobTemplateSpec
        """
        if job_template is None:
            raise ValueError("Invalid value for `job_template`, must not be `None`")

        self._job_template = job_template

    @property
    def schedule(self):
        """
        Gets the schedule of this V2alpha1CronJobSpec.
        The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.

        :return: The schedule of this V2alpha1CronJobSpec.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this V2alpha1CronJobSpec.
        The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.

        :param schedule: The schedule of this V2alpha1CronJobSpec.
        :type: str
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")

        self._schedule = schedule

    @property
    def starting_deadline_seconds(self):
        """
        Gets the starting_deadline_seconds of this V2alpha1CronJobSpec.
        Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.

        :return: The starting_deadline_seconds of this V2alpha1CronJobSpec.
        :rtype: int
        """
        return self._starting_deadline_seconds

    @starting_deadline_seconds.setter
    def starting_deadline_seconds(self, starting_deadline_seconds):
        """
        Sets the starting_deadline_seconds of this V2alpha1CronJobSpec.
        Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.

        :param starting_deadline_seconds: The starting_deadline_seconds of this V2alpha1CronJobSpec.
        :type: int
        """

        self._starting_deadline_seconds = starting_deadline_seconds

    @property
    def successful_jobs_history_limit(self):
        """
        Gets the successful_jobs_history_limit of this V2alpha1CronJobSpec.
        The number of successful finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified.

        :return: The successful_jobs_history_limit of this V2alpha1CronJobSpec.
        :rtype: int
        """
        return self._successful_jobs_history_limit

    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, successful_jobs_history_limit):
        """
        Sets the successful_jobs_history_limit of this V2alpha1CronJobSpec.
        The number of successful finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified.

        :param successful_jobs_history_limit: The successful_jobs_history_limit of this V2alpha1CronJobSpec.
        :type: int
        """

        self._successful_jobs_history_limit = successful_jobs_history_limit

    @property
    def suspend(self):
        """
        Gets the suspend of this V2alpha1CronJobSpec.
        This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.

        :return: The suspend of this V2alpha1CronJobSpec.
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """
        Sets the suspend of this V2alpha1CronJobSpec.
        This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.

        :param suspend: The suspend of this V2alpha1CronJobSpec.
        :type: bool
        """

        self._suspend = suspend

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V2alpha1CronJobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
