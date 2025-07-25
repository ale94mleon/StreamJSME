import React, { useCallback, useEffect, useMemo, useState } from "react"
import { Jsme } from "@loschmidt/jsme-react"
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"

/**
 * Streamlit component for JSME molecule editor.
 *
 * @param {ComponentProps} props - Props from Streamlit
 * @param {Object} props.args - Arguments from Python
 * @param {string} props.args.smiles - Initial SMILES string
 * @param {boolean} props.disabled - Disabled state
 * @param {Object} props.theme - Streamlit theme
 * @returns {React.ReactElement}
 */

interface PythonArgs {
  smiles: string
  height: number
  width: number
  margin: number
  src?: string
}

function App({ args, disabled, theme }: ComponentProps): React.ReactElement {
  const { smiles, height, width, margin, src }: PythonArgs = args
  const isFocused = useState(false)

  // Callback for molecule change
  const handleChange = useCallback((newSmiles: string) => {
    Streamlit.setComponentValue(newSmiles)
  }, [])

  const style: React.CSSProperties = useMemo(() => {
    if (!theme) return {}
    const borderStyling = `1px solid ${isFocused ? theme.primaryColor : "gray"}`
    return { border: borderStyling, outline: borderStyling }
  }, [theme, isFocused])

  useEffect(() => {
    Streamlit.setFrameHeight()
  }, [style, theme])

  return (
    <div
      style={{ height: `${height + margin}px`, width: `${width + margin}px` }}
    >
      <Jsme
        src={src}
        height={height}
        width={width}
        smiles={smiles}
        options="oldlook, star"
        onChange={handleChange}
        disabled={disabled}
      />
    </div>
  )
}

export default withStreamlitConnection(App)
