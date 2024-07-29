from scipy import stats

from data_analysis_functions import (total_charges_by_age_group,
                                     total_charges_by_partner,
                                     total_charges_by_dependents,
                                     total_charges_by_phone_service,
                                     total_charges_by_internet_service,
                                     total_charges_by_streaming_tv,
                                     )

t_test_functions = {
    'senior_citizen': total_charges_by_age_group,
    'partner': total_charges_by_partner,
    'dependents': total_charges_by_dependents,
    'phone_service': total_charges_by_phone_service,
    'internet_service': total_charges_by_internet_service,
    'streaming_tv': total_charges_by_streaming_tv
}


def t_hypothesis_test(variable):
    variable = variable.lower().strip()
    t_test_function = t_test_functions.get(variable)
    t_test = t_test_function()
    yes, no = t_test

    yes_total_charges_mean = round(yes.mean(), 2)
    no_tv_total_charges_mean = round(no.mean(), 2)

    t_stat, p_value = stats.ttest_ind(yes, no, alternative='greater')

    return yes_total_charges_mean, no_tv_total_charges_mean, round(t_stat, 2), p_value
