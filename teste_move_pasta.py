      return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        GnssTimeSuggestion that = (GnssTimeSuggestion) o;
        return Objects.equals(mUtcTime, that.mUtcTime);
    }

    @Override
    public int hashCode() {
        return Objects.hash(mUtcTime);
    }

    @Override
    public String toString() {
        return "GnssTimeSuggestion{"
                + "mUtcTime=" + mUtcTime
                + ", mDebugInfo=" + mDebugInfo
                + '}';
    }
}
                                                                                                                                                                                                                                      