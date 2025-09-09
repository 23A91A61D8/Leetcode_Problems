// Last updated: 09/09/2025, 14:18:29
class Solution {
    public String defangIPaddr(String address) {
        return address.replace(".","[.]");
    }
}