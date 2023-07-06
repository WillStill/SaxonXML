<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math" exclude-result-prefixes="xs math"
    version="3.0">

    <!--    <xsl:output method="xml" indent="yes"/> -->

    <xsl:variable name="dataColl" as="document-node()+" select="collection('data/?select=*.xml')"/>

    <xsl:variable name="sequenceNumbList" as="xs:string+" select="$dataColl//*/@sequence => sort()"/>



    <xsl:template match="/">
        <xsl:for-each select="$dataColl">
            <xsl:variable name="currentFile" as="document-node()" select="current()"/>

            <xsl:result-document href="{$currentFile//DeviceStream/@name}.xml" method="xml"
                indent="yes">
                <xsl:variable name="sequenceNumbList" as="xs:string*"
                    select="current()//*/@sequence => sort()"/>

                <root>
                    <metadata>
                        <machName>
                            <xsl:value-of
                                select="$currentFile//DeviceStream[not(@name = 'Agent')]/@name"/>
                        </machName>
                        <time>
                            <xsl:value-of select="current-dateTime()"/>
                        </time>
                    </metadata>
                    <data>


                        <xsl:for-each select="$sequenceNumbList">


                            <xsl:variable name="currentEle" as="element()"
                                select="$currentFile//*[@sequence = current()]"/>



                            <xsl:element name="{$currentEle/name()}">




                                <xsl:attribute name="num">
                                    <xsl:value-of select="current()"/>
                                </xsl:attribute>
                                <xsl:for-each select="$currentEle/@*">
                                    <xsl:attribute name="{current()/name()}">
                                        <xsl:value-of select="current()"/>
                                    </xsl:attribute>
                                </xsl:for-each>




                                
                                <xsl:apply-templates select="$currentEle"/>


                            </xsl:element>
                        </xsl:for-each>

                    </data>
                </root>

            </xsl:result-document>

        </xsl:for-each>



    </xsl:template>



</xsl:stylesheet>
