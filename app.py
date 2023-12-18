import streamlit as st
import pandas as pd
from faker import Faker

import base64
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

def generate_local_profile(number, locale, random_seed=200):
    local_fake = Faker(locale)
    data = [local_fake.simple_profile() for i in range(number)]
    df = pd.DataFrame(data)
    return df

def make_downloadable_df_format(data, format_type="csv"):
    if format_type == "json":
        datafile = data.to_json()
    else:
        datafile = data.to_csv(index=False)
    
    b64 = base64.b64encode(datafile.encode()).decode()
    st.markdown("### Download File ###")
    new_filename = "fake_dataset_{}.{}".format(timestr, format_type)
    href = f'<a href="data:file/{format_type};base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)

def main():
    st.title("Fake Data Generator")
    menu = ["Home", "Customise", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Simple Profile Generator")
        num_to_gen = st.sidebar.number_input("Number", 10, 5000)
        locale_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
        locale = st.sidebar.multiselect("Locale", locale_providers, default='en_US')
        df = generate_local_profile(num_to_gen, locale)
        dataformat = st.sidebar.selectbox("Save As ", ["csv", "json"])

        st.dataframe(df)
        with st.expander("Download File"):
            make_downloadable_df_format(df, dataformat)



    elif choice == "Customise":
        st.subheader("Select Custom Fields")
        num_to_gen = st.sidebar.number_input("Number", 10, 5000)
        locale_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
        locale = st.sidebar.multiselect("Locale", locale_providers, default='en_US')
        dataformat = st.sidebar.selectbox("Save As ", ["csv", "json"])

        profile_option_list = ["username", "mail", "name"]
        profile_fields = st.sidebar.multiselect("Fields", profile_option_list, default='username')
        custome_fake = Faker(locale)
        with st.expander("View as JSON"):
            for i in range(num_to_gen):
                st.write(custome_fake.profile(fields=profile_fields))
        data = [custome_fake.profile(fields=profile_fields) for i in range(num_to_gen)]
        df = pd.DataFrame(data)
        st.dataframe(df)
        with st.expander("Download File"):
            make_downloadable_df_format(df, dataformat)


    else:
        st.subheader("About")

if __name__ == '__main__':
    main()