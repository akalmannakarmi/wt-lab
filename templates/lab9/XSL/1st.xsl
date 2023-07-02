<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/class">
<html>
<body>
<table border="1.0" cellspacing="3">
<tr>
    <th>FirstName</th>
    <th>LastName</th>
    <th>NickName</th>
</tr>
<xsl:for-each select="student">
<tr>
<td><xsl:value-of select="FirstName"/></td>
<td><xsl:value-of select="LastName"/></td>
<td><xsl:value-of select="NickName"/></td>
</tr>
</xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>