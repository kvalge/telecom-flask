from scipy import stats

from data_analysis_functions import (total_charges_by_tv_service,
                                     total_charges_by_partner,
                                     total_charges_by_phone_service)


def tv_service_t_test():
    has_tv_service, has_not_tv_service = total_charges_by_tv_service()

    has_tv_total_charges_mean = round(has_tv_service.mean(), 2)
    has_not_tv_total_charges_mean = round(has_not_tv_service.mean(), 2)

    t_stat, p_value = stats.ttest_ind(has_tv_service, has_not_tv_service, alternative='greater')

    return has_tv_total_charges_mean, has_not_tv_total_charges_mean, round(t_stat, 2), p_value


def partner_t_test():
    has_partner, has_not_partner = total_charges_by_partner()

    has_partner_total_charges_mean = round(has_partner.mean(), 2)
    has_not_partner_total_charges_mean = round(has_not_partner.mean(), 2)

    t_stat, p_value = stats.ttest_ind(has_partner, has_not_partner, alternative='greater')

    return has_partner_total_charges_mean, has_not_partner_total_charges_mean, round(t_stat, 2), p_value


def phone_service_t_test():
    has_phone, has_not_phone = total_charges_by_phone_service()

    has_phone_total_charges_mean = round(has_phone.mean(), 2)
    has_not_phone_total_charges_mean = round(has_not_phone.mean(), 2)

    t_stat, p_value = stats.ttest_ind(has_phone, has_not_phone, alternative='greater')

    return has_phone_total_charges_mean, has_not_phone_total_charges_mean, round(t_stat, 2), p_value
