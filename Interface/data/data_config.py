#coding:utf-8
'''
封装获取常量的方法
'''
class global_var:
    #case_id
    Id = '0'
    Name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'
#获取caseid
def get_id():
    return global_var.Id

#获取case名称
def get_name():
    return global_var.Name

#获取url
def get_url():
    return global_var.url

#
def get_run():
    return global_var.run

def get_request_way():
    return global_var.request_way

def get_header():
    return global_var.header

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_field_depend():
    return global_var.field_depend

def get_data():
    return global_var.data

def get_expect():
    return global_var.expect

def get_result():
    return global_var.result

def get_header_value():
    header ={
        "Content-Type":"application/json",
        "cookie":"saml-session=ed65a318-d255-45ea-9189-d65a7b386f61; PolkaServiceProvider.Identity=CfDJ8HtpO5MIRMhPoERs0uSxYiAoK2j9ekjXdSxBFT1EvHH0QIVL4u1DmtVI1lh1YdUTLmtjiDhEQL-mJbKvCd7ckEOGwSnGPSp8CBV7ncmh_mGNqe4c1CdTgNFog7t5DsyGgqivBTsrFzAOBS6umEwa3j3utQgVe-TpOhvvL83gAEI17j-jHJNKi2yQun_Q4Xbvz6gxAJQqVnUcOR71hnlzCJYS5qQg8Dcg-I8kAWIq3i5TuDj-XuGNUObQP98iV0ns0NfbbrgveC2s8A0YTkQyFdivLBVTLY0kJ13zhG048cVrwdjo5voe8PwdvAE8eQRpX3jhmd0GJGWNotSN1ZKlS3LFmjfNXKAYY0PL63Fzd314g1HXBD_MGu0UxJFUYIR9VH6YSyNcZPGDuhdyk9eaEp3FgfXIsLP6Vvnx8SEiVjyMLVhPWdQn1ZXPxGPe5R82BGaF5sOKu5B03h1t5SpJJ9aqDK0zuFCuMhJ4amC2dbPDf5ThCU8NcL2DS3dwRjUHNmOd_fwjbPTlxGqmuNEDOKg; _sm_au_c=iVV5ppF261882j7r0f; SERVERID=65f153570a80f4a98ab8c11e721dc430|1541990243|1541983826"
    }
    return header


