class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        m = {}
        mr = {}
        m_cells = {
            'a1': {}, 'a2': {}, 'a3': {}, 
            'b1': {}, 'b2': {}, 'b3': {}, 
            'c1': {}, 'c2': {}, 'c3': {}
        }
        
        for ir, l in enumerate(board):
            row_check = {}
            for ic, l2 in enumerate(l):                
                tmp = m.get(ic, {})
                if l2 != '.' and l2 in tmp.keys():
                    return False
                else:                
                    tmp[l2] = 0
                    m[ic] = tmp
            
                if l2 != '.' and l2 in row_check.keys():
                    return False
                else:
                    row_check[l2] = 0                    
                try:
                    if ir in (0,1,2):
                        m_cells = self.check_m_blcok('a', m_cells, l2, ic)
                    if ir in (3,4,5):
                        m_cells = self.check_m_blcok('b', m_cells, l2, ic)
                    if ir in (6,7,8):
                        m_cells = self.check_m_blcok('c', m_cells, l2, ic)
                except Exception:
                    print('exc')
                    return False
        return True

    def check_m_blcok(self, block_name, m_cells, l2, ic):
        if ic in (0,1,2):
            m_cells = self.check_block(block_name + '1', m_cells, l2)
        if ic in (3,4,5):
            m_cells = self.check_block(block_name + '2', m_cells, l2)
        if ic in (6,7,8):
            m_cells = self.check_block(block_name + '3', m_cells, l2)
        return m_cells
        

    def check_block(self, block_name, mp, key):
        if key != '.' and key in mp[block_name].keys():
            print(mp)
            raise Exception()
        else:
            mp[block_name][key] = 0
        return mp

        