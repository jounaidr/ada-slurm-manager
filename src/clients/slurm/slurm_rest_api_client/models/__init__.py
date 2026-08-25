"""Contains all the data models used in inputs/outputs"""

from .dbv_0037_account import Dbv0037Account
from .dbv_0037_account_info import Dbv0037AccountInfo
from .dbv_0037_account_response import Dbv0037AccountResponse
from .dbv_0037_association import Dbv0037Association
from .dbv_0037_association_default import Dbv0037AssociationDefault
from .dbv_0037_association_max import Dbv0037AssociationMax
from .dbv_0037_association_max_jobs import Dbv0037AssociationMaxJobs
from .dbv_0037_association_max_jobs_per import Dbv0037AssociationMaxJobsPer
from .dbv_0037_association_max_per import Dbv0037AssociationMaxPer
from .dbv_0037_association_max_per_account import Dbv0037AssociationMaxPerAccount
from .dbv_0037_association_max_tres import Dbv0037AssociationMaxTres
from .dbv_0037_association_max_tres_group import Dbv0037AssociationMaxTresGroup
from .dbv_0037_association_max_tres_minutes import Dbv0037AssociationMaxTresMinutes
from .dbv_0037_association_max_tres_minutes_per import Dbv0037AssociationMaxTresMinutesPer
from .dbv_0037_association_max_tres_per import Dbv0037AssociationMaxTresPer
from .dbv_0037_association_min import Dbv0037AssociationMin
from .dbv_0037_association_short_info import Dbv0037AssociationShortInfo
from .dbv_0037_association_usage import Dbv0037AssociationUsage
from .dbv_0037_associations_info import Dbv0037AssociationsInfo
from .dbv_0037_cluster_info import Dbv0037ClusterInfo
from .dbv_0037_cluster_info_associations import Dbv0037ClusterInfoAssociations
from .dbv_0037_cluster_info_controller import Dbv0037ClusterInfoController
from .dbv_0037_config_info import Dbv0037ConfigInfo
from .dbv_0037_config_response import Dbv0037ConfigResponse
from .dbv_0037_coordinator_info import Dbv0037CoordinatorInfo
from .dbv_0037_diag import Dbv0037Diag
from .dbv_0037_diag_statistics import Dbv0037DiagStatistics
from .dbv_0037_diag_statistics_rollups_item import Dbv0037DiagStatisticsRollupsItem
from .dbv_0037_diag_statistics_rp_cs_item import Dbv0037DiagStatisticsRPCsItem
from .dbv_0037_diag_statistics_rp_cs_item_time import Dbv0037DiagStatisticsRPCsItemTime
from .dbv_0037_diag_statistics_users_item import Dbv0037DiagStatisticsUsersItem
from .dbv_0037_diag_statistics_users_item_time import Dbv0037DiagStatisticsUsersItemTime
from .dbv_0037_error import Dbv0037Error
from .dbv_0037_job import Dbv0037Job
from .dbv_0037_job_array import Dbv0037JobArray
from .dbv_0037_job_array_limits import Dbv0037JobArrayLimits
from .dbv_0037_job_array_limits_max import Dbv0037JobArrayLimitsMax
from .dbv_0037_job_array_limits_max_running import Dbv0037JobArrayLimitsMaxRunning
from .dbv_0037_job_comment import Dbv0037JobComment
from .dbv_0037_job_exit_code import Dbv0037JobExitCode
from .dbv_0037_job_exit_code_signal import Dbv0037JobExitCodeSignal
from .dbv_0037_job_het import Dbv0037JobHet
from .dbv_0037_job_het_job_id import Dbv0037JobHetJobId
from .dbv_0037_job_het_job_offset import Dbv0037JobHetJobOffset
from .dbv_0037_job_info import Dbv0037JobInfo
from .dbv_0037_job_mcs import Dbv0037JobMcs
from .dbv_0037_job_required import Dbv0037JobRequired
from .dbv_0037_job_reservation import Dbv0037JobReservation
from .dbv_0037_job_state import Dbv0037JobState
from .dbv_0037_job_step import Dbv0037JobStep
from .dbv_0037_job_step_cpu import Dbv0037JobStepCPU
from .dbv_0037_job_step_cpu_requested_frequency import Dbv0037JobStepCPURequestedFrequency
from .dbv_0037_job_step_nodes import Dbv0037JobStepNodes
from .dbv_0037_job_step_statistics import Dbv0037JobStepStatistics
from .dbv_0037_job_step_statistics_cpu import Dbv0037JobStepStatisticsCPU
from .dbv_0037_job_step_statistics_energy import Dbv0037JobStepStatisticsEnergy
from .dbv_0037_job_step_step import Dbv0037JobStepStep
from .dbv_0037_job_step_step_het import Dbv0037JobStepStepHet
from .dbv_0037_job_step_task import Dbv0037JobStepTask
from .dbv_0037_job_step_tasks import Dbv0037JobStepTasks
from .dbv_0037_job_step_time import Dbv0037JobStepTime
from .dbv_0037_job_step_time_system import Dbv0037JobStepTimeSystem
from .dbv_0037_job_step_time_total import Dbv0037JobStepTimeTotal
from .dbv_0037_job_step_time_user import Dbv0037JobStepTimeUser
from .dbv_0037_job_step_tres import Dbv0037JobStepTres
from .dbv_0037_job_step_tres_consumed import Dbv0037JobStepTresConsumed
from .dbv_0037_job_step_tres_requested import Dbv0037JobStepTresRequested
from .dbv_0037_job_time import Dbv0037JobTime
from .dbv_0037_job_time_system import Dbv0037JobTimeSystem
from .dbv_0037_job_time_total import Dbv0037JobTimeTotal
from .dbv_0037_job_time_user import Dbv0037JobTimeUser
from .dbv_0037_job_tres import Dbv0037JobTres
from .dbv_0037_job_wckey import Dbv0037JobWckey
from .dbv_0037_qos import Dbv0037Qos
from .dbv_0037_qos_info import Dbv0037QosInfo
from .dbv_0037_qos_limits import Dbv0037QosLimits
from .dbv_0037_qos_limits_max import Dbv0037QosLimitsMax
from .dbv_0037_qos_limits_max_accruing import Dbv0037QosLimitsMaxAccruing
from .dbv_0037_qos_limits_max_accruing_per import Dbv0037QosLimitsMaxAccruingPer
from .dbv_0037_qos_limits_max_jobs import Dbv0037QosLimitsMaxJobs
from .dbv_0037_qos_limits_max_jobs_active_jobs import Dbv0037QosLimitsMaxJobsActiveJobs
from .dbv_0037_qos_limits_max_jobs_active_jobs_per import Dbv0037QosLimitsMaxJobsActiveJobsPer
from .dbv_0037_qos_limits_max_tres import Dbv0037QosLimitsMaxTres
from .dbv_0037_qos_limits_max_tres_minutes import Dbv0037QosLimitsMaxTresMinutes
from .dbv_0037_qos_limits_max_tres_minutes_per import Dbv0037QosLimitsMaxTresMinutesPer
from .dbv_0037_qos_limits_max_tres_per import Dbv0037QosLimitsMaxTresPer
from .dbv_0037_qos_limits_max_wall_clock import Dbv0037QosLimitsMaxWallClock
from .dbv_0037_qos_limits_max_wall_clock_per import Dbv0037QosLimitsMaxWallClockPer
from .dbv_0037_qos_limits_min import Dbv0037QosLimitsMin
from .dbv_0037_qos_limits_min_tres import Dbv0037QosLimitsMinTres
from .dbv_0037_qos_limits_min_tres_per import Dbv0037QosLimitsMinTresPer
from .dbv_0037_qos_preempt import Dbv0037QosPreempt
from .dbv_0037_response_account_delete import Dbv0037ResponseAccountDelete
from .dbv_0037_response_association_delete import Dbv0037ResponseAssociationDelete
from .dbv_0037_response_associations import Dbv0037ResponseAssociations
from .dbv_0037_response_cluster_add import Dbv0037ResponseClusterAdd
from .dbv_0037_response_cluster_delete import Dbv0037ResponseClusterDelete
from .dbv_0037_response_qos_delete import Dbv0037ResponseQosDelete
from .dbv_0037_response_tres import Dbv0037ResponseTres
from .dbv_0037_response_user_delete import Dbv0037ResponseUserDelete
from .dbv_0037_response_user_update import Dbv0037ResponseUserUpdate
from .dbv_0037_response_wckey_add import Dbv0037ResponseWckeyAdd
from .dbv_0037_response_wckey_delete import Dbv0037ResponseWckeyDelete
from .dbv_0037_tres_info import Dbv0037TresInfo
from .dbv_0037_tres_list_item import Dbv0037TresListItem
from .dbv_0037_user import Dbv0037User
from .dbv_0037_user_associations import Dbv0037UserAssociations
from .dbv_0037_user_default import Dbv0037UserDefault
from .dbv_0037_user_info import Dbv0037UserInfo
from .dbv_0037_wckey import Dbv0037Wckey
from .dbv_0037_wckey_info import Dbv0037WckeyInfo
from .dbv_0038_account import Dbv0038Account
from .dbv_0038_account_info import Dbv0038AccountInfo
from .dbv_0038_account_response import Dbv0038AccountResponse
from .dbv_0038_accounting import Dbv0038Accounting
from .dbv_0038_association import Dbv0038Association
from .dbv_0038_association_default import Dbv0038AssociationDefault
from .dbv_0038_association_max import Dbv0038AssociationMax
from .dbv_0038_association_max_jobs import Dbv0038AssociationMaxJobs
from .dbv_0038_association_max_jobs_per import Dbv0038AssociationMaxJobsPer
from .dbv_0038_association_max_per import Dbv0038AssociationMaxPer
from .dbv_0038_association_max_per_account import Dbv0038AssociationMaxPerAccount
from .dbv_0038_association_max_tres import Dbv0038AssociationMaxTres
from .dbv_0038_association_max_tres_minutes import Dbv0038AssociationMaxTresMinutes
from .dbv_0038_association_max_tres_minutes_per import Dbv0038AssociationMaxTresMinutesPer
from .dbv_0038_association_max_tres_per import Dbv0038AssociationMaxTresPer
from .dbv_0038_association_min import Dbv0038AssociationMin
from .dbv_0038_association_short_info import Dbv0038AssociationShortInfo
from .dbv_0038_association_usage import Dbv0038AssociationUsage
from .dbv_0038_associations_info import Dbv0038AssociationsInfo
from .dbv_0038_cluster_info import Dbv0038ClusterInfo
from .dbv_0038_cluster_info_associations import Dbv0038ClusterInfoAssociations
from .dbv_0038_cluster_info_controller import Dbv0038ClusterInfoController
from .dbv_0038_clusters_properties import Dbv0038ClustersProperties
from .dbv_0038_config_info import Dbv0038ConfigInfo
from .dbv_0038_config_response import Dbv0038ConfigResponse
from .dbv_0038_coordinator_info import Dbv0038CoordinatorInfo
from .dbv_0038_diag import Dbv0038Diag
from .dbv_0038_diag_statistics import Dbv0038DiagStatistics
from .dbv_0038_diag_statistics_rollups_item import Dbv0038DiagStatisticsRollupsItem
from .dbv_0038_diag_statistics_rp_cs_item import Dbv0038DiagStatisticsRPCsItem
from .dbv_0038_diag_statistics_rp_cs_item_time import Dbv0038DiagStatisticsRPCsItemTime
from .dbv_0038_diag_statistics_users_item import Dbv0038DiagStatisticsUsersItem
from .dbv_0038_diag_statistics_users_item_time import Dbv0038DiagStatisticsUsersItemTime
from .dbv_0038_error import Dbv0038Error
from .dbv_0038_job import Dbv0038Job
from .dbv_0038_job_array import Dbv0038JobArray
from .dbv_0038_job_array_limits import Dbv0038JobArrayLimits
from .dbv_0038_job_array_limits_max import Dbv0038JobArrayLimitsMax
from .dbv_0038_job_array_limits_max_running import Dbv0038JobArrayLimitsMaxRunning
from .dbv_0038_job_comment import Dbv0038JobComment
from .dbv_0038_job_exit_code import Dbv0038JobExitCode
from .dbv_0038_job_exit_code_signal import Dbv0038JobExitCodeSignal
from .dbv_0038_job_het import Dbv0038JobHet
from .dbv_0038_job_info import Dbv0038JobInfo
from .dbv_0038_job_mcs import Dbv0038JobMcs
from .dbv_0038_job_required import Dbv0038JobRequired
from .dbv_0038_job_reservation import Dbv0038JobReservation
from .dbv_0038_job_state import Dbv0038JobState
from .dbv_0038_job_step import Dbv0038JobStep
from .dbv_0038_job_step_cpu import Dbv0038JobStepCPU
from .dbv_0038_job_step_cpu_requested_frequency import Dbv0038JobStepCPURequestedFrequency
from .dbv_0038_job_step_nodes import Dbv0038JobStepNodes
from .dbv_0038_job_step_statistics import Dbv0038JobStepStatistics
from .dbv_0038_job_step_statistics_cpu import Dbv0038JobStepStatisticsCPU
from .dbv_0038_job_step_statistics_energy import Dbv0038JobStepStatisticsEnergy
from .dbv_0038_job_step_step import Dbv0038JobStepStep
from .dbv_0038_job_step_step_het import Dbv0038JobStepStepHet
from .dbv_0038_job_step_tasks import Dbv0038JobStepTasks
from .dbv_0038_job_step_time import Dbv0038JobStepTime
from .dbv_0038_job_step_time_system import Dbv0038JobStepTimeSystem
from .dbv_0038_job_step_time_total import Dbv0038JobStepTimeTotal
from .dbv_0038_job_step_time_user import Dbv0038JobStepTimeUser
from .dbv_0038_job_step_tres import Dbv0038JobStepTres
from .dbv_0038_job_step_tres_consumed import Dbv0038JobStepTresConsumed
from .dbv_0038_job_step_tres_requested import Dbv0038JobStepTresRequested
from .dbv_0038_job_time import Dbv0038JobTime
from .dbv_0038_job_time_system import Dbv0038JobTimeSystem
from .dbv_0038_job_time_total import Dbv0038JobTimeTotal
from .dbv_0038_job_time_user import Dbv0038JobTimeUser
from .dbv_0038_job_tres import Dbv0038JobTres
from .dbv_0038_job_wckey import Dbv0038JobWckey
from .dbv_0038_meta import Dbv0038Meta
from .dbv_0038_meta_plugin import Dbv0038MetaPlugin
from .dbv_0038_meta_slurm import Dbv0038MetaSlurm
from .dbv_0038_meta_slurm_version import Dbv0038MetaSlurmVersion
from .dbv_0038_qos import Dbv0038Qos
from .dbv_0038_qos_info import Dbv0038QosInfo
from .dbv_0038_qos_limits import Dbv0038QosLimits
from .dbv_0038_qos_limits_max import Dbv0038QosLimitsMax
from .dbv_0038_qos_limits_max_accruing import Dbv0038QosLimitsMaxAccruing
from .dbv_0038_qos_limits_max_accruing_per import Dbv0038QosLimitsMaxAccruingPer
from .dbv_0038_qos_limits_max_jobs import Dbv0038QosLimitsMaxJobs
from .dbv_0038_qos_limits_max_jobs_active_jobs import Dbv0038QosLimitsMaxJobsActiveJobs
from .dbv_0038_qos_limits_max_jobs_active_jobs_per import Dbv0038QosLimitsMaxJobsActiveJobsPer
from .dbv_0038_qos_limits_max_tres import Dbv0038QosLimitsMaxTres
from .dbv_0038_qos_limits_max_tres_minutes import Dbv0038QosLimitsMaxTresMinutes
from .dbv_0038_qos_limits_max_tres_minutes_per import Dbv0038QosLimitsMaxTresMinutesPer
from .dbv_0038_qos_limits_max_tres_per import Dbv0038QosLimitsMaxTresPer
from .dbv_0038_qos_limits_max_wall_clock import Dbv0038QosLimitsMaxWallClock
from .dbv_0038_qos_limits_max_wall_clock_per import Dbv0038QosLimitsMaxWallClockPer
from .dbv_0038_qos_limits_min import Dbv0038QosLimitsMin
from .dbv_0038_qos_limits_min_tres import Dbv0038QosLimitsMinTres
from .dbv_0038_qos_limits_min_tres_per import Dbv0038QosLimitsMinTresPer
from .dbv_0038_qos_preempt import Dbv0038QosPreempt
from .dbv_0038_response_account_delete import Dbv0038ResponseAccountDelete
from .dbv_0038_response_associations import Dbv0038ResponseAssociations
from .dbv_0038_response_associations_delete import Dbv0038ResponseAssociationsDelete
from .dbv_0038_response_cluster_add import Dbv0038ResponseClusterAdd
from .dbv_0038_response_cluster_delete import Dbv0038ResponseClusterDelete
from .dbv_0038_response_qos import Dbv0038ResponseQos
from .dbv_0038_response_qos_delete import Dbv0038ResponseQosDelete
from .dbv_0038_response_tres import Dbv0038ResponseTres
from .dbv_0038_response_user_delete import Dbv0038ResponseUserDelete
from .dbv_0038_response_user_update import Dbv0038ResponseUserUpdate
from .dbv_0038_response_wckey_add import Dbv0038ResponseWckeyAdd
from .dbv_0038_response_wckey_delete import Dbv0038ResponseWckeyDelete
from .dbv_0038_set_config import Dbv0038SetConfig
from .dbv_0038_tres_info import Dbv0038TresInfo
from .dbv_0038_tres_list_item import Dbv0038TresListItem
from .dbv_0038_tres_update import Dbv0038TresUpdate
from .dbv_0038_update_account import Dbv0038UpdateAccount
from .dbv_0038_update_qos import Dbv0038UpdateQos
from .dbv_0038_update_users import Dbv0038UpdateUsers
from .dbv_0038_user import Dbv0038User
from .dbv_0038_user_default import Dbv0038UserDefault
from .dbv_0038_user_info import Dbv0038UserInfo
from .dbv_0038_wckey import Dbv0038Wckey
from .dbv_0038_wckey_info import Dbv0038WckeyInfo
from .dbv_0039_account_info import Dbv0039AccountInfo
from .dbv_0039_clusters_info import Dbv0039ClustersInfo
from .dbv_0039_diag import Dbv0039Diag
from .dbv_0039_error import Dbv0039Error
from .dbv_0039_meta import Dbv0039Meta
from .dbv_0039_meta_plugin import Dbv0039MetaPlugin
from .dbv_0039_meta_slurm import Dbv0039MetaSlurm
from .dbv_0039_meta_slurm_version import Dbv0039MetaSlurmVersion
from .dbv_0039_response_associations_delete import Dbv0039ResponseAssociationsDelete
from .dbv_0039_tres_info import Dbv0039TresInfo
from .dbv_0039_tres_update import Dbv0039TresUpdate
from .dbv_0039_update_users import Dbv0039UpdateUsers
from .dbv_0039_user_info import Dbv0039UserInfo
from .dbv_0039_warning import Dbv0039Warning
from .dbv_0039_wckey_info import Dbv0039WckeyInfo
from .slurm_v0039_cancel_job_signal import SlurmV0039CancelJobSignal
from .slurmdb_v0039_get_account_with_deleted import SlurmdbV0039GetAccountWithDeleted
from .slurmdb_v0039_get_accounts_with_deleted import SlurmdbV0039GetAccountsWithDeleted
from .slurmdb_v0039_get_jobs_disable_wait_for_result import SlurmdbV0039GetJobsDisableWaitForResult
from .slurmdb_v0039_get_jobs_skip_steps import SlurmdbV0039GetJobsSkipSteps
from .slurmdb_v0039_get_qos_with_deleted import SlurmdbV0039GetQosWithDeleted
from .slurmdb_v0039_get_single_qos_with_deleted import SlurmdbV0039GetSingleQosWithDeleted
from .slurmdb_v0039_get_user_with_deleted import SlurmdbV0039GetUserWithDeleted
from .slurmdb_v0039_get_users_with_deleted import SlurmdbV0039GetUsersWithDeleted
from .status import Status
from .v0037_diag import V0037Diag
from .v0037_diag_statistics import V0037DiagStatistics
from .v0037_error import V0037Error
from .v0037_job_properties import V0037JobProperties
from .v0037_job_properties_environment import V0037JobPropertiesEnvironment
from .v0037_job_properties_exclusive import V0037JobPropertiesExclusive
from .v0037_job_properties_gres_flags import V0037JobPropertiesGresFlags
from .v0037_job_properties_open_mode import V0037JobPropertiesOpenMode
from .v0037_job_resources import V0037JobResources
from .v0037_job_response_properties import V0037JobResponseProperties
from .v0037_job_submission import V0037JobSubmission
from .v0037_job_submission_response import V0037JobSubmissionResponse
from .v0037_jobs_response import V0037JobsResponse
from .v0037_node import V0037Node
from .v0037_node_allocation import V0037NodeAllocation
from .v0037_node_allocation_cores import V0037NodeAllocationCores
from .v0037_node_allocation_cpus import V0037NodeAllocationCpus
from .v0037_node_allocation_sockets import V0037NodeAllocationSockets
from .v0037_nodes_response import V0037NodesResponse
from .v0037_partition import V0037Partition
from .v0037_partitions_response import V0037PartitionsResponse
from .v0037_ping import V0037Ping
from .v0037_ping_ping import V0037PingPing
from .v0037_pings import V0037Pings
from .v0037_reservation import V0037Reservation
from .v0037_reservation_purge_completed import V0037ReservationPurgeCompleted
from .v0037_reservations_response import V0037ReservationsResponse
from .v0037_signal import V0037Signal
from .v0038_diag import V0038Diag
from .v0038_diag_rpcm import V0038DiagRpcm
from .v0038_diag_rpcu import V0038DiagRpcu
from .v0038_diag_statistics import V0038DiagStatistics
from .v0038_error import V0038Error
from .v0038_job_properties import V0038JobProperties
from .v0038_job_properties_environment import V0038JobPropertiesEnvironment
from .v0038_job_properties_exclusive import V0038JobPropertiesExclusive
from .v0038_job_properties_gres_flags import V0038JobPropertiesGresFlags
from .v0038_job_properties_open_mode import V0038JobPropertiesOpenMode
from .v0038_job_resources import V0038JobResources
from .v0038_job_response_properties import V0038JobResponseProperties
from .v0038_job_submission import V0038JobSubmission
from .v0038_job_submission_response import V0038JobSubmissionResponse
from .v0038_jobs_response import V0038JobsResponse
from .v0038_license import V0038License
from .v0038_licenses import V0038Licenses
from .v0038_meta import V0038Meta
from .v0038_meta_plugin import V0038MetaPlugin
from .v0038_meta_slurm import V0038MetaSlurm
from .v0038_meta_slurm_version import V0038MetaSlurmVersion
from .v0038_node import V0038Node
from .v0038_node_allocation import V0038NodeAllocation
from .v0038_node_allocation_sockets import V0038NodeAllocationSockets
from .v0038_node_allocation_sockets_cores import V0038NodeAllocationSocketsCores
from .v0038_nodes_response import V0038NodesResponse
from .v0038_partition import V0038Partition
from .v0038_partitions_response import V0038PartitionsResponse
from .v0038_ping import V0038Ping
from .v0038_ping_ping import V0038PingPing
from .v0038_pings import V0038Pings
from .v0038_reservation import V0038Reservation
from .v0038_reservation_purge_completed import V0038ReservationPurgeCompleted
from .v0038_reservations_response import V0038ReservationsResponse
from .v0038_signal import V0038Signal
from .v0039_account import V0039Account
from .v0039_account_flags_item import V0039AccountFlagsItem
from .v0039_accounting import V0039Accounting
from .v0039_accounting_allocated import V0039AccountingAllocated
from .v0039_assoc_flags_item import V0039AssocFlagsItem
from .v0039_assoc_id import V0039AssocId
from .v0039_assoc_short import V0039AssocShort
from .v0039_assoc_short_ptr import V0039AssocShortPtr
from .v0039_assoc_usage import V0039AssocUsage
from .v0039_assoc_usage_ptr import V0039AssocUsagePtr
from .v0039_cluster_rec import V0039ClusterRec
from .v0039_cluster_rec_associations import V0039ClusterRecAssociations
from .v0039_cluster_rec_controller import V0039ClusterRecController
from .v0039_cluster_rec_flags_item import V0039ClusterRecFlagsItem
from .v0039_controller_ping import V0039ControllerPing
from .v0039_coord import V0039Coord
from .v0039_cron_entry import V0039CronEntry
from .v0039_cron_entry_flags_item import V0039CronEntryFlagsItem
from .v0039_cron_entry_line import V0039CronEntryLine
from .v0039_cron_entry_ptr import V0039CronEntryPtr
from .v0039_cron_entry_ptr_flags_item import V0039CronEntryPtrFlagsItem
from .v0039_cron_entry_ptr_line import V0039CronEntryPtrLine
from .v0039_diag import V0039Diag
from .v0039_error import V0039Error
from .v0039_job_array_response_msg_item import V0039JobArrayResponseMsgItem
from .v0039_job_array_response_msg_ptr_item import V0039JobArrayResponseMsgPtrItem
from .v0039_job_desc_msg_cpu_binding_flags_item import V0039JobDescMsgCpuBindingFlagsItem
from .v0039_job_desc_msg_flags_item import V0039JobDescMsgFlagsItem
from .v0039_job_desc_msg_kill_warning_flags_item import V0039JobDescMsgKillWarningFlagsItem
from .v0039_job_desc_msg_mail_type_item import V0039JobDescMsgMailTypeItem
from .v0039_job_desc_msg_memory_binding_type_item import V0039JobDescMsgMemoryBindingTypeItem
from .v0039_job_desc_msg_open_mode_item import V0039JobDescMsgOpenModeItem
from .v0039_job_desc_msg_power_flags_item import V0039JobDescMsgPowerFlagsItem
from .v0039_job_desc_msg_profile_item import V0039JobDescMsgProfileItem
from .v0039_job_desc_msg_shared_item import V0039JobDescMsgSharedItem
from .v0039_job_desc_msg_x11_item import V0039JobDescMsgX11Item
from .v0039_job_exclusive_item import V0039JobExclusiveItem
from .v0039_job_exit_code import V0039JobExitCode
from .v0039_job_exit_code_signal import V0039JobExitCodeSignal
from .v0039_job_flags_item import V0039JobFlagsItem
from .v0039_job_info_flags_item import V0039JobInfoFlagsItem
from .v0039_job_info_mail_type_item import V0039JobInfoMailTypeItem
from .v0039_job_info_power_flags_item import V0039JobInfoPowerFlagsItem
from .v0039_job_info_profile_item import V0039JobInfoProfileItem
from .v0039_job_info_shared_item import V0039JobInfoSharedItem
from .v0039_job_info_show_flags_item import V0039JobInfoShowFlagsItem
from .v0039_job_res import V0039JobRes
from .v0039_job_res_ptr import V0039JobResPtr
from .v0039_job_submission_response import V0039JobSubmissionResponse
from .v0039_job_update_response import V0039JobUpdateResponse
from .v0039_license import V0039License
from .v0039_licenses_info import V0039LicensesInfo
from .v0039_meta import V0039Meta
from .v0039_meta_plugin import V0039MetaPlugin
from .v0039_meta_slurm import V0039MetaSlurm
from .v0039_meta_slurm_version import V0039MetaSlurmVersion
from .v0039_node_next_state_after_reboot_item import V0039NodeNextStateAfterRebootItem
from .v0039_node_state_item import V0039NodeStateItem
from .v0039_pings import V0039Pings
from .v0039_qos_flags_item import V0039QosFlagsItem
from .v0039_qos_preempt_mode_item import V0039QosPreemptModeItem
from .v0039_reservation_core_spec import V0039ReservationCoreSpec
from .v0039_reservation_info_flags_item import V0039ReservationInfoFlagsItem
from .v0039_rollup_stats_item import V0039RollupStatsItem
from .v0039_rollup_stats_item_type import V0039RollupStatsItemType
from .v0039_rollup_stats_ptr_item import V0039RollupStatsPtrItem
from .v0039_rollup_stats_ptr_item_type import V0039RollupStatsPtrItemType
from .v0039_slurm_step_id import V0039SlurmStepId
from .v0039_stats_msg import V0039StatsMsg
from .v0039_stats_msg_rpcs_by_type_item import V0039StatsMsgRpcsByTypeItem
from .v0039_stats_msg_rpcs_by_user_item import V0039StatsMsgRpcsByUserItem
from .v0039_stats_rec import V0039StatsRec
from .v0039_stats_rec_ptr import V0039StatsRecPtr
from .v0039_stats_rpc import V0039StatsRpc
from .v0039_stats_rpc_time import V0039StatsRpcTime
from .v0039_stats_user import V0039StatsUser
from .v0039_stats_user_time import V0039StatsUserTime
from .v0039_tres import V0039Tres
from .v0039_update_node_msg_state_item import V0039UpdateNodeMsgStateItem
from .v0039_user import V0039User
from .v0039_user_administrator_level_item import V0039UserAdministratorLevelItem
from .v0039_user_default import V0039UserDefault
from .v0039_user_flags_item import V0039UserFlagsItem
from .v0039_warning import V0039Warning
from .v0039_wckey import V0039Wckey
from .v0039_wckey_flags_item import V0039WckeyFlagsItem
from .v0039_wckey_tag import V0039WckeyTag
from .v0039_wckey_tag_flags_item import V0039WckeyTagFlagsItem

__all__ = (
    "Dbv0037Account",
    "Dbv0037AccountInfo",
    "Dbv0037AccountResponse",
    "Dbv0037Association",
    "Dbv0037AssociationDefault",
    "Dbv0037AssociationMax",
    "Dbv0037AssociationMaxJobs",
    "Dbv0037AssociationMaxJobsPer",
    "Dbv0037AssociationMaxPer",
    "Dbv0037AssociationMaxPerAccount",
    "Dbv0037AssociationMaxTres",
    "Dbv0037AssociationMaxTresGroup",
    "Dbv0037AssociationMaxTresMinutes",
    "Dbv0037AssociationMaxTresMinutesPer",
    "Dbv0037AssociationMaxTresPer",
    "Dbv0037AssociationMin",
    "Dbv0037AssociationShortInfo",
    "Dbv0037AssociationsInfo",
    "Dbv0037AssociationUsage",
    "Dbv0037ClusterInfo",
    "Dbv0037ClusterInfoAssociations",
    "Dbv0037ClusterInfoController",
    "Dbv0037ConfigInfo",
    "Dbv0037ConfigResponse",
    "Dbv0037CoordinatorInfo",
    "Dbv0037Diag",
    "Dbv0037DiagStatistics",
    "Dbv0037DiagStatisticsRollupsItem",
    "Dbv0037DiagStatisticsRPCsItem",
    "Dbv0037DiagStatisticsRPCsItemTime",
    "Dbv0037DiagStatisticsUsersItem",
    "Dbv0037DiagStatisticsUsersItemTime",
    "Dbv0037Error",
    "Dbv0037Job",
    "Dbv0037JobArray",
    "Dbv0037JobArrayLimits",
    "Dbv0037JobArrayLimitsMax",
    "Dbv0037JobArrayLimitsMaxRunning",
    "Dbv0037JobComment",
    "Dbv0037JobExitCode",
    "Dbv0037JobExitCodeSignal",
    "Dbv0037JobHet",
    "Dbv0037JobHetJobId",
    "Dbv0037JobHetJobOffset",
    "Dbv0037JobInfo",
    "Dbv0037JobMcs",
    "Dbv0037JobRequired",
    "Dbv0037JobReservation",
    "Dbv0037JobState",
    "Dbv0037JobStep",
    "Dbv0037JobStepCPU",
    "Dbv0037JobStepCPURequestedFrequency",
    "Dbv0037JobStepNodes",
    "Dbv0037JobStepStatistics",
    "Dbv0037JobStepStatisticsCPU",
    "Dbv0037JobStepStatisticsEnergy",
    "Dbv0037JobStepStep",
    "Dbv0037JobStepStepHet",
    "Dbv0037JobStepTask",
    "Dbv0037JobStepTasks",
    "Dbv0037JobStepTime",
    "Dbv0037JobStepTimeSystem",
    "Dbv0037JobStepTimeTotal",
    "Dbv0037JobStepTimeUser",
    "Dbv0037JobStepTres",
    "Dbv0037JobStepTresConsumed",
    "Dbv0037JobStepTresRequested",
    "Dbv0037JobTime",
    "Dbv0037JobTimeSystem",
    "Dbv0037JobTimeTotal",
    "Dbv0037JobTimeUser",
    "Dbv0037JobTres",
    "Dbv0037JobWckey",
    "Dbv0037Qos",
    "Dbv0037QosInfo",
    "Dbv0037QosLimits",
    "Dbv0037QosLimitsMax",
    "Dbv0037QosLimitsMaxAccruing",
    "Dbv0037QosLimitsMaxAccruingPer",
    "Dbv0037QosLimitsMaxJobs",
    "Dbv0037QosLimitsMaxJobsActiveJobs",
    "Dbv0037QosLimitsMaxJobsActiveJobsPer",
    "Dbv0037QosLimitsMaxTres",
    "Dbv0037QosLimitsMaxTresMinutes",
    "Dbv0037QosLimitsMaxTresMinutesPer",
    "Dbv0037QosLimitsMaxTresPer",
    "Dbv0037QosLimitsMaxWallClock",
    "Dbv0037QosLimitsMaxWallClockPer",
    "Dbv0037QosLimitsMin",
    "Dbv0037QosLimitsMinTres",
    "Dbv0037QosLimitsMinTresPer",
    "Dbv0037QosPreempt",
    "Dbv0037ResponseAccountDelete",
    "Dbv0037ResponseAssociationDelete",
    "Dbv0037ResponseAssociations",
    "Dbv0037ResponseClusterAdd",
    "Dbv0037ResponseClusterDelete",
    "Dbv0037ResponseQosDelete",
    "Dbv0037ResponseTres",
    "Dbv0037ResponseUserDelete",
    "Dbv0037ResponseUserUpdate",
    "Dbv0037ResponseWckeyAdd",
    "Dbv0037ResponseWckeyDelete",
    "Dbv0037TresInfo",
    "Dbv0037TresListItem",
    "Dbv0037User",
    "Dbv0037UserAssociations",
    "Dbv0037UserDefault",
    "Dbv0037UserInfo",
    "Dbv0037Wckey",
    "Dbv0037WckeyInfo",
    "Dbv0038Account",
    "Dbv0038AccountInfo",
    "Dbv0038Accounting",
    "Dbv0038AccountResponse",
    "Dbv0038Association",
    "Dbv0038AssociationDefault",
    "Dbv0038AssociationMax",
    "Dbv0038AssociationMaxJobs",
    "Dbv0038AssociationMaxJobsPer",
    "Dbv0038AssociationMaxPer",
    "Dbv0038AssociationMaxPerAccount",
    "Dbv0038AssociationMaxTres",
    "Dbv0038AssociationMaxTresMinutes",
    "Dbv0038AssociationMaxTresMinutesPer",
    "Dbv0038AssociationMaxTresPer",
    "Dbv0038AssociationMin",
    "Dbv0038AssociationShortInfo",
    "Dbv0038AssociationsInfo",
    "Dbv0038AssociationUsage",
    "Dbv0038ClusterInfo",
    "Dbv0038ClusterInfoAssociations",
    "Dbv0038ClusterInfoController",
    "Dbv0038ClustersProperties",
    "Dbv0038ConfigInfo",
    "Dbv0038ConfigResponse",
    "Dbv0038CoordinatorInfo",
    "Dbv0038Diag",
    "Dbv0038DiagStatistics",
    "Dbv0038DiagStatisticsRollupsItem",
    "Dbv0038DiagStatisticsRPCsItem",
    "Dbv0038DiagStatisticsRPCsItemTime",
    "Dbv0038DiagStatisticsUsersItem",
    "Dbv0038DiagStatisticsUsersItemTime",
    "Dbv0038Error",
    "Dbv0038Job",
    "Dbv0038JobArray",
    "Dbv0038JobArrayLimits",
    "Dbv0038JobArrayLimitsMax",
    "Dbv0038JobArrayLimitsMaxRunning",
    "Dbv0038JobComment",
    "Dbv0038JobExitCode",
    "Dbv0038JobExitCodeSignal",
    "Dbv0038JobHet",
    "Dbv0038JobInfo",
    "Dbv0038JobMcs",
    "Dbv0038JobRequired",
    "Dbv0038JobReservation",
    "Dbv0038JobState",
    "Dbv0038JobStep",
    "Dbv0038JobStepCPU",
    "Dbv0038JobStepCPURequestedFrequency",
    "Dbv0038JobStepNodes",
    "Dbv0038JobStepStatistics",
    "Dbv0038JobStepStatisticsCPU",
    "Dbv0038JobStepStatisticsEnergy",
    "Dbv0038JobStepStep",
    "Dbv0038JobStepStepHet",
    "Dbv0038JobStepTasks",
    "Dbv0038JobStepTime",
    "Dbv0038JobStepTimeSystem",
    "Dbv0038JobStepTimeTotal",
    "Dbv0038JobStepTimeUser",
    "Dbv0038JobStepTres",
    "Dbv0038JobStepTresConsumed",
    "Dbv0038JobStepTresRequested",
    "Dbv0038JobTime",
    "Dbv0038JobTimeSystem",
    "Dbv0038JobTimeTotal",
    "Dbv0038JobTimeUser",
    "Dbv0038JobTres",
    "Dbv0038JobWckey",
    "Dbv0038Meta",
    "Dbv0038MetaPlugin",
    "Dbv0038MetaSlurm",
    "Dbv0038MetaSlurmVersion",
    "Dbv0038Qos",
    "Dbv0038QosInfo",
    "Dbv0038QosLimits",
    "Dbv0038QosLimitsMax",
    "Dbv0038QosLimitsMaxAccruing",
    "Dbv0038QosLimitsMaxAccruingPer",
    "Dbv0038QosLimitsMaxJobs",
    "Dbv0038QosLimitsMaxJobsActiveJobs",
    "Dbv0038QosLimitsMaxJobsActiveJobsPer",
    "Dbv0038QosLimitsMaxTres",
    "Dbv0038QosLimitsMaxTresMinutes",
    "Dbv0038QosLimitsMaxTresMinutesPer",
    "Dbv0038QosLimitsMaxTresPer",
    "Dbv0038QosLimitsMaxWallClock",
    "Dbv0038QosLimitsMaxWallClockPer",
    "Dbv0038QosLimitsMin",
    "Dbv0038QosLimitsMinTres",
    "Dbv0038QosLimitsMinTresPer",
    "Dbv0038QosPreempt",
    "Dbv0038ResponseAccountDelete",
    "Dbv0038ResponseAssociations",
    "Dbv0038ResponseAssociationsDelete",
    "Dbv0038ResponseClusterAdd",
    "Dbv0038ResponseClusterDelete",
    "Dbv0038ResponseQos",
    "Dbv0038ResponseQosDelete",
    "Dbv0038ResponseTres",
    "Dbv0038ResponseUserDelete",
    "Dbv0038ResponseUserUpdate",
    "Dbv0038ResponseWckeyAdd",
    "Dbv0038ResponseWckeyDelete",
    "Dbv0038SetConfig",
    "Dbv0038TresInfo",
    "Dbv0038TresListItem",
    "Dbv0038TresUpdate",
    "Dbv0038UpdateAccount",
    "Dbv0038UpdateQos",
    "Dbv0038UpdateUsers",
    "Dbv0038User",
    "Dbv0038UserDefault",
    "Dbv0038UserInfo",
    "Dbv0038Wckey",
    "Dbv0038WckeyInfo",
    "Dbv0039AccountInfo",
    "Dbv0039ClustersInfo",
    "Dbv0039Diag",
    "Dbv0039Error",
    "Dbv0039Meta",
    "Dbv0039MetaPlugin",
    "Dbv0039MetaSlurm",
    "Dbv0039MetaSlurmVersion",
    "Dbv0039ResponseAssociationsDelete",
    "Dbv0039TresInfo",
    "Dbv0039TresUpdate",
    "Dbv0039UpdateUsers",
    "Dbv0039UserInfo",
    "Dbv0039Warning",
    "Dbv0039WckeyInfo",
    "SlurmdbV0039GetAccountsWithDeleted",
    "SlurmdbV0039GetAccountWithDeleted",
    "SlurmdbV0039GetJobsDisableWaitForResult",
    "SlurmdbV0039GetJobsSkipSteps",
    "SlurmdbV0039GetQosWithDeleted",
    "SlurmdbV0039GetSingleQosWithDeleted",
    "SlurmdbV0039GetUsersWithDeleted",
    "SlurmdbV0039GetUserWithDeleted",
    "SlurmV0039CancelJobSignal",
    "Status",
    "V0037Diag",
    "V0037DiagStatistics",
    "V0037Error",
    "V0037JobProperties",
    "V0037JobPropertiesEnvironment",
    "V0037JobPropertiesExclusive",
    "V0037JobPropertiesGresFlags",
    "V0037JobPropertiesOpenMode",
    "V0037JobResources",
    "V0037JobResponseProperties",
    "V0037JobsResponse",
    "V0037JobSubmission",
    "V0037JobSubmissionResponse",
    "V0037Node",
    "V0037NodeAllocation",
    "V0037NodeAllocationCores",
    "V0037NodeAllocationCpus",
    "V0037NodeAllocationSockets",
    "V0037NodesResponse",
    "V0037Partition",
    "V0037PartitionsResponse",
    "V0037Ping",
    "V0037PingPing",
    "V0037Pings",
    "V0037Reservation",
    "V0037ReservationPurgeCompleted",
    "V0037ReservationsResponse",
    "V0037Signal",
    "V0038Diag",
    "V0038DiagRpcm",
    "V0038DiagRpcu",
    "V0038DiagStatistics",
    "V0038Error",
    "V0038JobProperties",
    "V0038JobPropertiesEnvironment",
    "V0038JobPropertiesExclusive",
    "V0038JobPropertiesGresFlags",
    "V0038JobPropertiesOpenMode",
    "V0038JobResources",
    "V0038JobResponseProperties",
    "V0038JobsResponse",
    "V0038JobSubmission",
    "V0038JobSubmissionResponse",
    "V0038License",
    "V0038Licenses",
    "V0038Meta",
    "V0038MetaPlugin",
    "V0038MetaSlurm",
    "V0038MetaSlurmVersion",
    "V0038Node",
    "V0038NodeAllocation",
    "V0038NodeAllocationSockets",
    "V0038NodeAllocationSocketsCores",
    "V0038NodesResponse",
    "V0038Partition",
    "V0038PartitionsResponse",
    "V0038Ping",
    "V0038PingPing",
    "V0038Pings",
    "V0038Reservation",
    "V0038ReservationPurgeCompleted",
    "V0038ReservationsResponse",
    "V0038Signal",
    "V0039Account",
    "V0039AccountFlagsItem",
    "V0039Accounting",
    "V0039AccountingAllocated",
    "V0039AssocFlagsItem",
    "V0039AssocId",
    "V0039AssocShort",
    "V0039AssocShortPtr",
    "V0039AssocUsage",
    "V0039AssocUsagePtr",
    "V0039ClusterRec",
    "V0039ClusterRecAssociations",
    "V0039ClusterRecController",
    "V0039ClusterRecFlagsItem",
    "V0039ControllerPing",
    "V0039Coord",
    "V0039CronEntry",
    "V0039CronEntryFlagsItem",
    "V0039CronEntryLine",
    "V0039CronEntryPtr",
    "V0039CronEntryPtrFlagsItem",
    "V0039CronEntryPtrLine",
    "V0039Diag",
    "V0039Error",
    "V0039JobArrayResponseMsgItem",
    "V0039JobArrayResponseMsgPtrItem",
    "V0039JobDescMsgCpuBindingFlagsItem",
    "V0039JobDescMsgFlagsItem",
    "V0039JobDescMsgKillWarningFlagsItem",
    "V0039JobDescMsgMailTypeItem",
    "V0039JobDescMsgMemoryBindingTypeItem",
    "V0039JobDescMsgOpenModeItem",
    "V0039JobDescMsgPowerFlagsItem",
    "V0039JobDescMsgProfileItem",
    "V0039JobDescMsgSharedItem",
    "V0039JobDescMsgX11Item",
    "V0039JobExclusiveItem",
    "V0039JobExitCode",
    "V0039JobExitCodeSignal",
    "V0039JobFlagsItem",
    "V0039JobInfoFlagsItem",
    "V0039JobInfoMailTypeItem",
    "V0039JobInfoPowerFlagsItem",
    "V0039JobInfoProfileItem",
    "V0039JobInfoSharedItem",
    "V0039JobInfoShowFlagsItem",
    "V0039JobRes",
    "V0039JobResPtr",
    "V0039JobSubmissionResponse",
    "V0039JobUpdateResponse",
    "V0039License",
    "V0039LicensesInfo",
    "V0039Meta",
    "V0039MetaPlugin",
    "V0039MetaSlurm",
    "V0039MetaSlurmVersion",
    "V0039NodeNextStateAfterRebootItem",
    "V0039NodeStateItem",
    "V0039Pings",
    "V0039QosFlagsItem",
    "V0039QosPreemptModeItem",
    "V0039ReservationCoreSpec",
    "V0039ReservationInfoFlagsItem",
    "V0039RollupStatsItem",
    "V0039RollupStatsItemType",
    "V0039RollupStatsPtrItem",
    "V0039RollupStatsPtrItemType",
    "V0039SlurmStepId",
    "V0039StatsMsg",
    "V0039StatsMsgRpcsByTypeItem",
    "V0039StatsMsgRpcsByUserItem",
    "V0039StatsRec",
    "V0039StatsRecPtr",
    "V0039StatsRpc",
    "V0039StatsRpcTime",
    "V0039StatsUser",
    "V0039StatsUserTime",
    "V0039Tres",
    "V0039UpdateNodeMsgStateItem",
    "V0039User",
    "V0039UserAdministratorLevelItem",
    "V0039UserDefault",
    "V0039UserFlagsItem",
    "V0039Warning",
    "V0039Wckey",
    "V0039WckeyFlagsItem",
    "V0039WckeyTag",
    "V0039WckeyTagFlagsItem",
)
