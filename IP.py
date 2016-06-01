class IP:
    """Transforms IP and MAC to a decimal and binary form"""
    def __init__(self, IP):
        self.IP = str(IP)

    def get_ip(self):
        """Allocates IP"""
        only_IP = ''
        for i in self.IP:
            if i == '/':
                break
            else:
                only_IP = only_IP + i
        return only_IP

    def get_mac(self):
        """Allocates MAC"""
        only_mac = ''
        for i in self.IP[::-1]:
            if i == '/':
                break
            else:
                only_mac = only_mac + i
        only_mac = int(only_mac[::-1])
        return only_mac

    def ip_ten(self):
        """Transforms IP to a decimal form"""
        only_IP = self.get_ip()
        new_only_ip = ''
        res = 0
        n = 3
        for i in only_IP:
            if i == '.':
                res += int(new_only_ip) * (256**n)
                new_only_ip = ''
                n -= 1
            else:
                new_only_ip = new_only_ip + i
        res += int(new_only_ip) * (256**0)
        return res

    def ip_two(self):
        """Transforms IP to a binary form"""
        only_IP = self.get_ip()
        in_two = ''
        part_only_IP = ''
        all_reverse_number_new = ''
        for i in only_IP:
            if i == '.':
                for count in range(8):
                    if int(part_only_IP) == 0:
                        in_two += '0'
                    else:
                        number_new = int(part_only_IP) // 2
                        rest = int(part_only_IP) - number_new*2
                        in_two += str(rest)
                        part_only_IP = number_new
                reverse_number_new = in_two[::-1] + '.'
                all_reverse_number_new += reverse_number_new
                part_only_IP = ''
                reverse_number_new = ''
                in_two = ''
            else:
                part_only_IP = part_only_IP + i
        for count in range(8):
            if int(part_only_IP) == 0:
                in_two += '0'
            else:
                number_new = int(part_only_IP) // 2
                rest = int(part_only_IP) - number_new*2
                in_two += str(rest)
                part_only_IP = number_new
        reverse_number_new = in_two[::-1]
        all_reverse_number_new += reverse_number_new
        return (all_reverse_number_new)

    def mac_two(self):
        """Transforms MAC to a decimal form"""
        only_mac = self.get_mac()
        mac_inter = ''
        mac_two_real = ''
        if only_mac > 0:
            for i in range(only_mac):
                mac_inter += '1'
                p = i
            for j in range(p, 32):
                mac_inter += '0'
            for y in range(4):
                for t in range(8):
                    mac_two_real += mac_inter[t+y*8]
                mac_two_real += '.'
        else:
            for j in range(32):
                mac_inter += '0'
            for y in range(4):
                for t in range(8):
                    mac_two_real += mac_inter[t+y*8]
                mac_two_real += '.'
        mac_two_real = mac_two_real[0:35]
        return mac_two_real

    def mac_ten(self):
        """Transforms MAC to a binary form"""
        mac_two_real = self.mac_two()
        part_new_a = ''
        k = 0
        all_sum = 0
        all_mac_ten = ''
        for i in  mac_two_real:
            if i == '.':
                for i in part_new_a[::-1]:
                    if int(i) == 0:
                        k += 1
                    else:
                        sum = 2 ** k
                        all_sum += sum
                        k += 1
                all_mac_ten += str(all_sum) + '.'
                part_new_a = ''
                all_sum = 0
                k = 0
            else:
                part_new_a += i
        for i in part_new_a[::-1]:
            if int(i) == 0:
                k += 1
            else:
                sum = 2 ** k
                all_sum += sum
                k += 1
        all_mac_ten += str(all_sum)
        return all_mac_ten


letter = IP('152.128.34.85/27')
print ('ip_ten =', letter.ip_ten())
print ('ip_two =', letter.ip_two())
print ('mac_two =', letter.mac_two())
print ('mac_ten =', letter.mac_ten())