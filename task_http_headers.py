import json


def http_headers_to_json(fail_in, fail_out):

    data_r = {}

    with open(fail_in, 'r') as x:

        if x.read(8) == "HTTP/1.1":
            x.seek(0)
            y = x.readline()
            y = y.strip('\n')
            y = y.split(" ")
            if y[1] == '301':
                    data_r = {
                        "protocol": y[0],
                        "status_code": y[1],
                        "status_message": y[2]+' ' + y[3]
                        }
            else:
                data_r = {
                    "protocol": y[0],
                    "status_code": y[1],
                    "status_message": y[2]
                    }

            for z in x:

                if len(z) > 1:
                    z = z.strip('\n')
                    z = z.split(': ')
                    data_r[z[0]] = z[1]

        else:
            x.seek(0)
            y = x.readline()
            y = y.strip('\n')
            y = y.split(" ")
            data_r = {
                "method": y[0],
                "uri": y[1],
                "protocol": y[2]
                }

            for z in x:

                if len(z) > 1:
                    z = z.strip('\n')
                    z = z.split(': ')
                    data_r[z[0]] = z[1]

        with open(fail_out, 'w') as a:
                json.dump(data_r, a)
