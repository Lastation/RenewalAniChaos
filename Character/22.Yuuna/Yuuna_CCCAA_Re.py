import variable as v;
import func.trig as trg;

function main(playerID)
{
   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] < 15)
         {         
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.MoveLoc(v.P_UnitID[playerID], playerID, 200 - 50 * (v.P_LoopMain[playerID] % 4), 50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "50 + 1n Tank");
            trg.SkillUnit(playerID, 1, "60 + 1n Danimoth");
            trg.MoveLoc(v.P_UnitID[playerID], playerID, -200 + 50 * (v.P_LoopMain[playerID] % 4), -50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "50 + 1n Tank");
            trg.SkillUnit(playerID, 1, "60 + 1n Danimoth");
            trg.MoveLoc(v.P_UnitID[playerID], playerID, 50 * (v.P_LoopMain[playerID] % 4), -200 + 50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "Protoss Dark Archon");
            trg.MoveLoc(v.P_UnitID[playerID], playerID, -50 * (v.P_LoopMain[playerID] % 4), 200 - 50 * (v.P_LoopMain[playerID] % 4));
            trg.SkillUnit(playerID, 1, "Protoss Dark Archon");

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            trg.Main_Wait(80);

            v.P_LoopMain[playerID] += 1;
         }
         else if (v.P_LoopMain[playerID] == 15)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Main_Wait(80);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] == 0)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, -50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, -50);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Main_Wait(240);

            v.P_LoopMain[playerID] += 1;
         }
         else if (v.P_LoopMain[playerID] == 1)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 100, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 150, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Zealot", 200, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 100, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 150, 200);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 100);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 150);
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 200, 200);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            trg.Main_Wait(240);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
         
      }
      else if (v.P_CountMain[playerID] == 2)
      {

         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         trg.SkillEnd();


      }


   }
}