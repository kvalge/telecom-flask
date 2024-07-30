from scipy import stats
from scipy.stats import mannwhitneyu

from data_analysis_functions import (total_charges_by_age_group,
                                     total_charges_by_partner,
                                     total_charges_by_dependents,
                                     total_charges_by_phone_service,
                                     total_charges_by_internet_service,
                                     total_charges_by_streaming_tv,
                                     total_charges_by_multiple_lines,
                                     total_charges_by_online_security,
                                     total_charges_by_online_backup,
                                     total_charges_by_device_protection,
                                     total_charges_by_tech_support,
                                     total_charges_by_streaming_movies,
                                     total_charges_by_paperless_billing
                                     )

functions_names = {
    'senior_citizen': total_charges_by_age_group,
    'partner': total_charges_by_partner,
    'dependents': total_charges_by_dependents,
    'phone_service': total_charges_by_phone_service,
    'internet_service': total_charges_by_internet_service,
    'streaming_tv': total_charges_by_streaming_tv,
    'multiple_lines': total_charges_by_multiple_lines,
    'online_security': total_charges_by_online_security,
    'online_backup': total_charges_by_online_backup,
    'device_protection': total_charges_by_device_protection,
    'tech_support': total_charges_by_tech_support,
    'streaming_movies': total_charges_by_streaming_movies,
    'paperless_billing': total_charges_by_paperless_billing,
}


def hypothesis_test(variable):
    variable = variable.lower().strip()
    test_function_name = functions_names.get(variable)
    hyp_test = test_function_name()
    yes, no = hyp_test

    yes_total_charges_mean = round(yes.mean(), 2)
    no_tv_total_charges_mean = round(no.mean(), 2)

    t_stat, ttest_p_value = stats.ttest_ind(yes, no, alternative='greater')
    u_stat, utest_p_value = mannwhitneyu(yes, no)

    return (yes_total_charges_mean,
            no_tv_total_charges_mean,
            round(t_stat, 2),
            ttest_p_value,
            round(u_stat, 2),
            utest_p_value)
