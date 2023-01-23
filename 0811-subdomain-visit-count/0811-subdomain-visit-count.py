class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        domain_count = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            
            count = int(count)
            domains = domain.split('.')
            
            for i in range(len(domains)):
                domain_count['.'.join(domains[i:])] += count
                
        return [ f'{count} {domain}' for domain, count in domain_count.items() ]
        
        
        