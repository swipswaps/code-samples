
""" domainForwarding -- 45 min
Domain name forwarding lets GoDaddy domain owners automatically redirect 
their site visitors to a different site URL. Sometimes the visitors have 
to go through multiple redirects before ending up on the correct site.

Using the DNS Manager, GoDaddy customers can view redirects in a simple 
visual format. One handy feature is the ability to group the domains by 
the final website they redirect to. Your task is to implement this feature.

For the given redirects list, organize its domains into groups where for 
a specific group each domain eventually redirects visitors to the same 
website.

Example

For

redirects = [["godaddy.net", "godaddy.com"], 
             ["godaddy.org", "godaddycares.com"], 
             ["godady.com", "godaddy.com"],
             ["godaddy.ne", "godaddy.net"]]

the output should be

domainForwarding(redirects) = 
[["godaddy.com", "godaddy.ne", "godaddy.net", "godady.com"], 
["godaddy.org", "godaddycares.com"]]

In the first group, "godaddy.ne" redirects to "godaddy.net", which in turn 
redirects to "godaddy.com". "godady.com" redirects visitors to "godaddy.com" 
as well.
In the second group, "godaddy.org" redirects visitors to "godaddycares.com".

Note, that domains in each group are sorted lexicographically and groups 
themselves are sorted lexicographically by the domain they redirect to. So 
in the example, the first group goes before the second because "godaddy.com" 
is lexicographically smaller than "godaddycares.com".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.string redirects

    Each of redirects[i] consists of two domains. The second element is 
    the domain to which the first element redirects. Each domain is a string 
    that may consist of lowercase English letters, hyphens ('-') and full 
    stops ('.').
    It is guaranteed that domain redirects do not contain cycles, i.e. it 
    is impossible to get back to the current site after any number of redirects. 
    It is also guaranteed that each domain redirects to no more than one another 
    domain, i.e. for each i ≠ j redirects[i][0] ≠ redirects[j][0].

    Guaranteed constraints:
    1 ≤ redirects.length ≤ 15,
    redirects[i].length == 2,
    1 ≤ redirects[i][j].length ≤ 25.

    [output] array.array.string
        Return the array of domain groups, such that each domain from 
        redirects belongs to one of the group, and domains from one group 
        redirect visitors to the same website. Arrange the domains in each 
        group in lexicographical order, and sort the groups by the domains 
        they redirect to (also lexicographically).
"""

def domainForwarding(redirects):
    set0, set1, dicLand, dicRed, result = set(), set(), {}, {}, []
    for d in redirects:
        dicRed[d[0]] = d[1]
        set0.add(d[0])
        set1.add(d[1])
    setLand = set1 - set0
    for d in setLand:
        dicLand[d] = []
    for d in dicRed.keys():
        if dicRed[d] in dicLand: dicLand[dicRed[d]].append(d)
        else:
            tmp = []
            while dicRed[d] not in dicLand:
                tmp.extend([d, dicRed[d]])
                d = dicRed[d]
            dicLand[dicRed[d]].extend(tmp)
    for d in sorted(dicLand.keys()):
        dicLand[d].append(d)
        result.append(sorted(list(set(dicLand[d]))))
    return result


print(domainForwarding([["godaddy.net", "godaddy.com"], 
             ["godaddy.org", "godaddycares.com"], 
             ["godady.com", "godaddy.com"],
             ["godaddy.ne", "godaddy.net"]])) 

"""
[["godaddy.com", "godaddy.ne", "godaddy.net", "godady.com"], 
["godaddy.org", "godaddycares.com"]]
"""
