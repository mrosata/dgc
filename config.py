CUSTOM_PATTERNS = {
    'GREEDY_DATA': '.*',
    'DATE_YMD': '%{YEAR}-%{MONTHNUM}-%{MONTHDAY}'
}

HEADER_LINES = 0

FILES = ['cf-logs.tsv', 'E3FS88YNWID5YK.2018-08-25-15.5c11fb30.tsv']

GROK_PATTERN = '%{DATE_YMD:ymd:date}\t%{TIME:time}\t%{HOSTNAME:location}\t(?:%{NUMBER:bytes:int}|-)\t\
%{IPORHOST:request_ip}\t%{WORD:method}\t(?:%{HOSTNAME:host}|-)\t(?:%{NOTSPACE:uri}|-)\t\
(?:%{INT:status:int}|-)\t%{NOTSPACE:referrer}\t%{NOTSPACE:user_agent}\t%{NOTSPACE:query_string}\t\
%{NOTSPACE:cookie}\t(?:%{WORD:result_type}|-)\t%{NOTSPACE:request_id}\t%{HOSTNAME:host_header}\t\
(?:%{NOTSPACE:request_protocol}|-)\t(?:%{INT:request_bytes:int}|-)\t%{NOTSPACE:time_taken:float}\t\
%{NOTSPACE:x_forwarded_for}\t%{NOTSPACE:ssl_protocol}\t%{NOTSPACE:ssl_cipher}\t%{NOTSPACE:response_result_type}\t\
%{NOTSPACE:http_version}\t%{NOTSPACE:file_status}\t%{NOTSPACE:encrypted_fields}'
