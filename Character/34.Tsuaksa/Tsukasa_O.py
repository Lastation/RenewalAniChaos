import variable as v;
import func.trig as trg;
import func.trigepic as epic;

function main(playerID)
{
   if (Deaths(CurrentPlayer, AtLeast, 1234, " `UniqueCoolTime"))
   {
      if (Deaths(CurrentPlayer, Exactly, 2160, " `UniqueCoolTime"))
      {
         trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 3, 50);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
      }
      else if (Deaths(CurrentPlayer, Exactly, 1235, " `UniqueCoolTime"))
      {
         trg.Shape_Dot(playerID, 1, "Kakaru (Twilight)", 0, 0);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
      }
      ModifyUnitHitPoints(All, " * Hunter Killer", playerID, "Anywhere", 100);
   }
}