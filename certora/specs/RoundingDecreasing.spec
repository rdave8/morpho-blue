// SPDX-License-Identifier: GPL-2.0-or-later

using Util as Util;

methods {
    function extSloads(bytes32[]) external returns bytes32[] => NONDET DELETE;

    function Util.libToAssetsDown(uint256, uint256, uint256) external returns uint256 envfree;
    function Util.libToSharesUp(uint256, uint256, uint256) external returns uint256 envfree;

    function MathLib.mulDivDown(uint256 a, uint256 b, uint256 c) internal returns uint256 => summaryMulDivDown(a, b, c);
    function MathLib.mulDivUp(uint256 a, uint256 b, uint256 c) internal returns uint256 => summaryMulDivUp(a, b, c);
}

function summaryMulDivUp(uint256 x, uint256 y, uint256 d) returns uint256 {
    // Safe require because the reference implementation would revert.
    return require_uint256((x * y + (d - 1)) / d);
}

function summaryMulDivDown(uint256 x, uint256 y, uint256 d) returns uint256 {
    // Safe require because the reference implementation would revert.
    return require_uint256((x * y) / d);
}

// Check that rounding down assets then rounding up resulting shares is less than or equal to the original assets.
// This is notably useful to know that it is possible to withdraw the expected assets without an underflow when subtracting shares.
rule roundDownUpIsDecreasing() {
    uint256 shares; uint256 totalSupplyAssets; uint256 totalSupplyShares;

    uint256 expectedAssets = Util.libToAssetsDown(shares, totalSupplyAssets, totalSupplyShares);
    uint256 withdrawnShares = Util.libToSharesUp(expectedAssets, totalSupplyAssets, totalSupplyShares);

    assert withdrawnShares <= shares;
}

rule roundUpDownIsIncreasing() {
    uint256 shares; uint256 totalSupplyAssets; uint256 totalSupplyShares;

    uint256 expectedAssets = Util.libToAssetsDown(shares, totalSupplyAssets, totalSupplyShares);
    uint256 withdrawnShares = Util.libToSharesUp(expectedAssets, totalSupplyAssets, totalSupplyShares);

    assert withdrawnShares <= shares;
}
